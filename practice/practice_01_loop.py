# 문제 1) 입력 된 단수를 출력하는 코드
#dan = int(input("단수: "))
#for i in range(1, 10):
#    print(f"{dan}x{i}={i*dan}")


# 문제 2) 2단부터 9단까지 출력 => 중첩for
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i}x{j}={i*j}")

# 문제 3) list a의 평균값을 계산하세요.
a = [1, 2, 3, 4, 5, 99, 87, 54, 2, 5, 4]
length = len(a)
total = 0
for i in a:
    total += i
result = total / length
print(round(result, 2))  #round(값, 소수점자리) : 반올림

# 문제 4) list b에서 최솟값 찾기!
b = [22, 1, 4, 7, 98]
num_min = 0
for i in range(5):
    for j in range(4):
        if b[j] > b[j+1]:
            c = b[j]
            b[j] = b[j+1]
            b[j+1] = c
num_min = b[0]
print(num_min)

# 문제 5) list c의 최솟값, 최대값 찾기
c = [2, 5, 7, 1, 8]
num_min = c[0]
num_max = c[0]
for i in c:
    if num_min > i:
        num_min = i
    if num_max < i:
        num_max = i


print(num_min)
print(num_max)

print("="*100)

# 문제 6)
# 사용자가 입력하는 값 -> 1, 2, 3,만 가능
# 사용자가 입력한 값 1, 2, 3 통과
# 아닌경우 다시 입력

#count = 0  # 틀린 횟수
# while True:
#    if count == 4:
#        print("프로그램을 사용할 수 없읍니다.")
#        break
#    num = int(input("값: "))
#    if num in [1, 2, 3]:
#        print(f"{num}을 입력하였습니다.")
#        break
#    else:
#        print("1, 2, 3의 값만 입력해주세요.")
#        count += 1

# 문제 7) 1부터 100까지 총합을 출력하는 코드
# for 문
sum = 0
for i in range(1, 101):
    sum += i
print(f"총합 for: {sum}")
ssum = 0
s = 1
while True:
    if s > 100:
        break
    ssum += s
    s += 1
print(f"총합 while: {ssum}")

