# WebCrawling(웹 크롤링)
#  - 웹 페이지에서 원하는 데이터를 수집하는 기술
#  - 데이터가 필요한 작업 -> 원하는 데이터가 없는 경우!
#                         (제공X, 다운X)
#   -> 웹 크롤링을 사용해서 직접 데이터를 수집
#  - 직업: 웹 크롤러(전문)
#  -      데이터 엔지니어(웹 크롤링 + @)

#  - 웹 크롤링 + 스케줄링 + 자동화

# 외부 라이브러리(다운로드 + import)
#  1.BeautifulSoup4(bs4)
#  2.Requests
#  3.Selenium

#  웹 페이지
#    - 정적 페이지(Requests + bs4) 첫번째 실행
#    - 동적 페이지(Selenium + bs4) 안될 시 실행

# conda env list -> basic check
# 없으면: conda create -n basic python=3.8
# conda activate basic
# pip install requests
# pip install selenium
# pip install beautiful4
# import requests
# import selenium
# from bs4 import BeautifulSoup

# 웹 프로그래밍 기초(속성)
#  - 프론트 엔드: 사용자 화면 개발
#  - 백 엔드: 서비스와 DB 개발
#  - 풀 스택: 프론트 엔드 + 백 엔드

# MVC 패턴
#  - VIEW(사용자 화면)(프론트)
#  - CONTROLLER(백)
#  - MODEL(데이터베이스: 저장)(백)

# 웹 페이지 화면 구현
#  - 웹 표준: HTML, CSS, Javascript
#  1.HTML: 프레임 구현
#  2.CSS: 디자인(색상, 크기, 모양, 등등)
#  3.Javascript: 동적 기능

# HTML 속성
#  - <tag></tag> 구현
#  - tag 종류: div, span, a, h4, etc...
#  - tag 종속관계
#    <div>  1           div > span -> 2, div span -> 2, 3
#      <span>  2
#        <span></span>  3
#      </span>
#      <span></span>  2
#    </div>
#    div: 부모
#     ㄴ  span: 자식
#    종속관계: 부모자식 (div > span: div태그의 자식 태그인 span)
#             자손(div span: div태그 안에 있는 모든 span)

#  선택자
#  1.ID(#): 유일한 선택자
#  2.CLASS(.): 복수 선택자

import requests
from bs4 import BeautifulSoup
url = "https://v.daum.net/v/20231101150335324"  # 수집하고 싶은 웹사이트 주소

# 1.URL에 접속해서 전체 소스코드 가져오기!
result = requests.get(url)
# status_code: 200(성공)
#              400~500번대 오류
# print(result)
# print(result.text)

# 2.전체 소스코드(requests) -> bs4
doc = BeautifulSoup(result.text, "html.parser")

# 3.원하는 정보 수집
title = doc.select("h3.tit_view")[0].get_text()
# select() -> 결과: List Type
print(f"제목: {title}")

# 경고: Tag 이름으로는 절대 수집 X
content_list = doc.select("div.article_view p")

content = ""
for p in content_list:
    content +=p.get_text()
print(f"본문: {content}")

# 기사 날짜 데이터 수집
reg_date = doc.select()
print(f"날짜: {reg_date}")




