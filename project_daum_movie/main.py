from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from datetime import datetime, timedelta
import math
import re
import time
from bs4 import BeautifulSoup

# Selenium + BeautifulSoup4
#  - Selenium: 전체 소스코드 가져오기(+동적으로 페이지 조작)
#  - BeautifulSoup4: 필요한 데이터만 Select

# **Selenium
#   - 웹브라우저 검사(Test) 도구 -> 데이터 수집
#   - 전용 브라우저를 동작(크롬, 파이어폭스, 등등)로 동작
#   - 전용 브라우저 Open -> 작업 -> 브라우저 Close(Default)

# ** Selenium 사용방법 2가지
#   1.직접 다운로드(크롬 브라우저)해서 사용
#     url: https://sites.google.com/chromium.org/driver/

# 2.실시간 다운로드 후 사용
options = Options()
# Selenium이 작업 완료 후에 전용 브라우저 종료 X
options.add_experimental_option("detach", True)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# URL 접속
url = "https://movie.daum.net/moviedb/grade?movieId=169137"
driver.get(url)
time.sleep(1)

# 페이지 소스 가져오기
doc_html = driver.page_source

doc = BeautifulSoup(doc_html, "html.parser")

# 영화 제목 수집
movie_title = doc.select("span.txt_tit")[0].get_text()
print(movie_title)

total_review_cnt = doc.select("span.txt_netizen")[0].get_text()
# (187명) 에서 숫자만 추출하는 방법
#   1. 문자열 슬라이싱 방법
#print(total_review_cnt[1:-2])
#   2. 정규식 사용한 방법
num_review = int(re.sub(r"[^~0-9]", "", total_review_cnt))
#print(num_review)

# 187 = 최초(10), 버튼1개(30개)
click_cnt = math.ceil((num_review - 10) / 30)

for i in range(click_cnt):
    # "평점 더보기" 버튼 클릭
    driver.find_element(By.CLASS_NAME, "link_fold").click()
    time.sleep(2)

# 전체 소스코드 가져오기2(평점이 모두 출력된 페이지)
doc_html = driver.page_source
doc = BeautifulSoup(doc_html, "html.parser")
review_list = doc.select("ul.list_comment > li")

print(f"전체리뷰 : {len(review_list)}")

for item in review_list:
    print("="*100)
    review_score = item.select("div.ratings")[0].get_text()
    print(f"  - 평점: {review_score}")
    review_content = item.select("p.desc_txt")[0].get_text().strip()
    # \n : 한 줄 개행
    # 수집한 리뷰가 개행 -> 문자열 안에 \n 포함
    review_content = re.sub("\n", "", review_content)
    print(f"  - 리뷰: {review_content}")
    review_writer = item.select("a.link_nick > span")[1].get_text()  # [댓글 작성자, 작성자, 댓글 모아보기]
    print(f"  - 작성자: {review_writer}")
    # 24시간 이내에 작성된 글은 날짜 -> 예: 21시간전, 17시간 전
    # 실제 날짜 표기법 -> 2023. 11. 17. 12:15
    # 표기법: 21시간 전 -> 2023. 11. 17. 12:15

    review_date = item.select("span.txt_date")[0].get_text()
    if len(review_date) < 7:
        # 예) 17시간전 -> 숫자만 추출: 17
        reg_hour = int(re.sub(r"[^~0-9]", "", review_date))
        # print(reg_hour)
        # print(datetime.now())
        # 예) 현재시간(2023. 11. 17. 12:29) - 18 = (2023. 11. 16 18:29:23.1231513)
        review_date = (datetime.now()-timedelta(hours=reg_hour))
        review_date = review_date.strftime("%Y. &m. %d. %H:%M")
        # 예) 2023. 11. 16 18:29:23.1231513 -> 2023. 11. 16. 18:29
    print(f"  - 날짜: {review_date}")
    # 21시간 전 잘못 뜨는 경우를 어떤 조건으로 찾을 수 있을지?
    #print("수정 필요!")




