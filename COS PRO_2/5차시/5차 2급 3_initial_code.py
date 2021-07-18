def solution(speed, cars):
    answer = 0
    for car in cars:
        if (int(speed*1.2) > car) and car >= int(speed*1.1):
            answer += 3
            print( answer )
        elif speed*1.3> car and car >= speed*1.2:
            answer += 5
            print(answer)
        elif speed*1.3>= car:
            answer += 7
            print(answer)
            print( speed*1.2 )
            print( speed*1.1 )
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
speed = 100 # 규정속도
cars = [110, 98, 125, 148, 120, 112, 89] # 자동차들의 속도
#위반 :  3  , 0 , 5  , 7  , 5  ,  3 , 0  => 23만원

ret = solution(speed, cars)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")