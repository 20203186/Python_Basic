# 조건문(Condition) : if~elif~else

# - 특정 조건을 만족하는 경우에만 수행할 작업이 있는 경우
# - 모든 조건은 boolean으로 표현 됨
# - 조건문의 경우 if, elif, else 블록 내 종속된 코드 들여쓰기
# - 모든 블록문의 시작점은 마지막에 :(콜론, colon) 추가
# - python에서 블록내에 코든느 반드시 들여쓰기(Tab) 강제

#if (조건) {                  if 조건1:
#    code                        code
#} else if (조건2) {          elif 조건2:
#    code                        code
#}

# 제어문 기본 문법
#    if 조건1:
#        code
#    elif 조건2:
#        code
#    elif 조건3:
#        code
#    else:
#        code

score = 95
if score >= 91 and score <= 100 :
    print("A")
elif score >= 81 :
    print("B")
elif score >= 71 :
    print("C")
elif score >= 61 :
    print("D")
else :
    print("F")

from datetime import datetime

born = input("당신이 태어난 년도를 입력하세요: ")
today = datetime.today().year
age = today - int(born) + 1

if age <= 26 and age >= 20:
    print("대학생")
elif age < 20 and age >= 17:
    print("고등학생")
elif age < 17 and age >= 14:
    print("중학생")
elif age < 14 and age >= 8:
    print("초등학생")
else:
    print("학생이 아닙니다.")


