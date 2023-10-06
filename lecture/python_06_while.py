# while 반복문
#  - 반복횟수를 모르는 경우
#  - 조건이 만족하는 동안 계속 반복
#  - 조건 True이면 무한 반복
#  - 조건 False이면 반복 종료
#  - while문에 조건 True => 무한 Loop문  (주의)
#    -> 반드시 break문과 함께 사용!

# while 기본 문법
# while 조건:
#      실행문

a = list(range(1, 6))
print(a)

i = 0  # index
while i < len(a):
    print(a[i])
    i += 1




