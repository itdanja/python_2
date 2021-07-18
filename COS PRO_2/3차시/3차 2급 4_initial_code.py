#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution( 단어목록 , 찾는단어 ):
    오타수 = 0
    
    for comp in words : # 단어목록 만큼 하나씩 반복 
        for x,y in zip( comp , word ) : # 검사단어=x , 찾는단어=y 
            if x !=y : # 검사단어와 찾는단어가 같지않으면 
                오타수 += 1 # 오타 증가
    return 오타수

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
words = ["CODE", "COED", "CDEO"]

word = "CODE"
ret = solution(words, word)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")