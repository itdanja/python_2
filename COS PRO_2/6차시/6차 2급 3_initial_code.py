#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(people):
    answer = [0, 0, 0, 0]
    for i in people:
        if i<95:
            answer[0]+=1
        if 95<=i<100:
            answer[1]+=1
        if 100<=i<105:
            answer[2]+=1
        if 105<=i:
            answer[3]+=1
    return answer



#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
people = [97, 102, 93, 100, 107] # 주문 사이즈
    #      M  L    S  , L  , XL  => 1  , 1 ,  , 2 , 1
ret = solution(people)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret, " 입니다.")