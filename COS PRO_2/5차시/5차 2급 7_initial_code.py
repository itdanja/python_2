def solution(stuffs):
    answer = 0
    small_counter, general_counter = 0, 0
    for s in stuffs: # 손님들의 물건 구매수
        if s > 3:   #  물건수 3초과이면
            general_counter += s # 일반계산대 += 물건수[1개당1분]
        else: # 물건수 3이하이면
            small_counter += s # 소량계산대 += 물건수[1개당1분]
    #if small_counter < general_counter :
    if small_counter > general_counter: # 소량계산대가 더 많으면
        answer = small_counter
    else:
        answer = general_counter
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 아래에는 잘못된 부분이 없으니 위의 코드만 수정하세요.
stuffs = [5, 3, 4, 2, 3, 2] # 손님들의 물건 구매수
ret = solution(stuffs)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")