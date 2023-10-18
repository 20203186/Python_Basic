max_car = 5  # 최대 5대
car_cnt = 0  # 주차된 차량 수 카운트

# 주차 타워 생성
# 1. List Comprehension
tower = ["" for i in range(max_car)]

# 2. for + list.append()
# for i in range(max_car):
#     tower.append("")
# 결과: ["", "", "", "", ""]
while True:
    print("="*50)
    print("== 주차 타워 시스템 ver1.1 ==")
    print("="*50)
    print("= 1.입고")
    print("= 2.출고")
    print("= 3.조회")
    print("= 4.종료")
    print("="*50)

    while True:
        select_num = int(input(">>번호: "))
        if 4 >= select_num >= 1:
            break
        else:
            print("MSG: 올바른 번호를 입력하세요.")

    if select_num == 1:     # 입고
        # 입고 1. 주차타워 공간 확인.
        if car_cnt < max_car:  # 입고
            car_num = input(">>입고: ")
            for i, car in enumerate(tower):
                if car == "":
                    tower[i] = car_num
                    car_cnt += 1
                    break
        else:
            print("MSG: 만석입니다.")
    elif select_num == 2:   # 출고
        # 1. 차량번호 입력받기
      if car_cnt > 0:
        car_num = input(">>출고: ")
        for i in range(max_car):
          if tower[i] == car_num:
            tower[i] = ""
            car_cnt -= 1
            print(f"{car_num} 차량이 출고되었습니다.")
            break
          elif tower[max_car-1] != car_num:
            print("해당 차량이 없습니다.")
            break
      else:
        print("*"*50)
        print("주차타워가 비어있습니다")
        # 2. 주차타워에서 차량번호 확인
        # 2-1. x -> 차 없음
        # 2-2. 출고(tower 값 => ""), (car_cnt -= 1)
    elif select_num == 3:   # 조회
        for i in range(max_car):
            print(f"{i+1}층 == {tower[i]}")
    elif select_num == 4:   # 종료
        print("MSG: 프로그램을 종료합니다.")
        exit()  # == break;
