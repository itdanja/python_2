
#문제4

#다음과 같이 import를 사용할 수 있습니다.
import math
def solution(words):
    # len(문자) : 문자길이
    answer = ""
    for w in words :
        if len(w) >= 5 : # 문자길이가 5글자 이상이면
            answer += w  #  문자1 += 문자2  => 문자1문자2 연결

    if len(answer) < 1 : # 5글자 문자가 하나도 없으면
        answer = "empty"
    return answer

        # my , is 을 제외한 5글자 이상 단어들끼리 이어 붙이기
words1 = ["my", "favorite", "color", "is", "violet"]
ret1 = solution(words1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret1, " 입니다.")

words2 = ["yes", "i", "am"]
ret2 = solution(words2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은 ", ret2, " 입니다.")