#문제2
def func_a(arr):  # 5의배수를 구하는 함수
    count = 0
    for n in arr:
        if n % 5 == 0: #   값 % 5 == 0   5의배수
            count += 1
    return count

def func_b(three, five): # 3의배수와 5의배수 개수 비교
    if three > five:        # 3배수개수 > 5배수개수
        return "three"
    elif three < five:      # 3배수개수 < 5배수개수
        return "five"
    else:                    # 3배수개수 == 5배수개수
        return "same"

def func_c(arr):  # 3의배수를 구하는 함수
    count = 0
    for n in arr:
        if n % 3 == 0:  #   값 % 3 == 0   3의 배수
            count += 1
    return count

def solution(arr):
    count_three = func_c(arr)
    count_five = func_a(arr)
    answer = func_b(count_three, count_five)
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
arr = [2, 3, 6, 9, 12, 15, 10, 20, 22, 25]
ret = solution(arr)
#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")