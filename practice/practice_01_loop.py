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

print(num_min)

