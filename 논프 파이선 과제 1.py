

def A():
    while True:
        a = int(input("첫 번째 숫자를 입력하세요: "))
        b = int(input("두 번째 숫자를 입력하세요: "))
        
        # 두 숫자를 비교하여 큰 값을 찾음
        if a - b>0:
           B = a
        elif a-b==0:
            B = a
        else:
            B = b
        
        # 큰 값이 1 이상 10 이하인지 확인하고 별표 출력
        if 1 <= B <= 10:
            print(f"입력한 두 숫자 중 큰 숫자는 {B}입니다.")
            print("*" * B)
            break  
        else:
            print("입력한 숫자 중 큰 수가 1 이상 10 이하의 범위에 있어야 합니다. 다시 입력하세요.")

# 함수 호출
A()
