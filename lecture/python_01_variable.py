# 주석(Comment) : 단순 메모, 개발 실행 X

# 출력 함수(print)
# - ()안의 값을 출력
# - 변수 값 확인용도 또는 메시지 출력용도
print("=" * 200)
print("Hello Python2023")


# 문자열 타입(String Type)
# - Python: '', "" -> String
# - C, Java; ''(Char), ""(String)

#참고 Escape Code
#- 문법 \ +@
#- 문자열 내의 일부 문자의 의미를 달리하여 특정한 효과 주기
#- 예) \n 한줄 개행, \t 탭 8칸 공백

print("Hello \n Python")
print("Hello \t Python")

# ctrl + shift +f10 실행

#공부 tip
# 몇 버전부터 나온기술(신기술) -> 신기술공부, 구 기술 공부 x
# 자료형 (Type)
# Python의 모든 자료형은 객체(object)
# Python에서 문자형(char)은 없다.
# C, Java 언어 문자형은 키보드 제어할 때 사용
# 1) 문자열(String): "Hello"
# 2) 정수형(int): 실수 1
# 3) 실수형(float): 3.14, 0.0, -2.2
# 4) 논리형(boolean): true, false

#ex) 다양한 종류의 자료형을 사용하는 이유?
#   - JAVA 정수형: byte, short, int, long
#   - Python 정수형: int
#   만들어진지 오래 된 언어는 다양한 종류의 자료형을 사용!
#   이유는: 자원(메모리)를 효율적으로 사용하기 위해서!
#   예: 자료형은 담을 수 있는 크기의 범위가 지정되어 있음
#   예를 들어서 int는(-100000 ~ 100000) 까지 담을 수 있다고 가정
#   그런데 우리 회사에서 특정값이 0~9만 사용!
#   int 를 사용하게 되면 메로리 낭비, 이런 경우 크기의 범위가 더 작은
#   자료형을 사용하면 좋음

# Python 동적 타이핑 언어 -> Python 실행 될 때 Type을 지정!
#   - type() 함수: ()안의 값의 type을 확인할 때 사용
print(type("ABC"))
print(type(123))

# 형 변환(Type Casting)
#   - Type Casting을 사용하면 값을 원하는 자료형으로 변환 가능
#   1) int(): 정수형으로 변환
#   2) float(): 실수형으로 변환
#   3) str(): 문자열형으로 변환
print("=" * 200)

# Type Casting 실습
int_a = 3
float_b = 3.14
str_c = "9.2"
str_float_d = "9.2"
# 1) 문자열 정수형("9") -> 정수형 (9)
print(int(str_int_c))
# 1-2) 문자열 정수형("9") -> 실수형 (9.0)
print(float(str_float_c))
# 2) 문자열 실수형("9.2") -> 정수형 (Error)
#print(int(str_int_d))
# 2-2) 문자열 실수형("9.2") -> 실수형 9.2
print(float(str_float_d))
# 3) 정수형 3 -> 실수형 3.0
print(float(int_a))
# 4) 정수형 3 -> 문자열 "3"
print(str(int_a))
# 5) 실수형 3.14 -> 정수형 3
print(int(float_b))
# 6) 실수형 3.14 -> 문자열 "3.14"
print(str(float_b))  #  코드 옆 주석 2칸 띄운 후 쓰기
# * float("Hello"), int("Hello") 형 변환 불가!

# Nonea
#  - 아무런 값을 갖지 않을 때 사용
#  - 일반적으로 변수가 초기값을 갖지 않게 변수만 생성하고 싶을 때 사용
#  - 기타 언어의 Null과 같은 의미로 사용!
#  예) student_name
student_name = None  # 적극 권장 X(절대 사용 금지)
student_name = ""  #  적극 권장 O
#  이유? "Null Pointer Exception" Error 개발자 공포의 대상!!

#  기본자료형(Primitibe Type) : 변수에 값이 저장
#   - int num = 4;
#  객체 자료형(Reference Type) : 변수에 값의 주소가 저장
#   - String name = "10";
#  * Java : 기본, 객체 모두 사용
#  * Python : 객체만 사용

#  C언어 변수 생성 -> int b; == 변수 생성, 값x
#  Python 변수 생성 -> b == 변수 호출

#  변수(Variable)
#   -  변수: 하나의 값을 저장할 수 있는 메모리 공간
print("=" * 200)
num = 4
num = 10
print(num)  # 출력: 10

# - 변수 생성 및 초기화
# num = 5  # 문법
# 대입연산자(=) : 우측의 값을 좌측에 저장
# 동등연산자(==) : Equal