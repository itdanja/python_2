
# 팰린드롬 : noon : 첫번째 글자 == 마지막글자
        # racecar : 두번째 글자 == 마지막앞글자
#문제8 : .[점] 과 ' '[공백]을 제외한 문자 비교하기 위해   or => and
def solution( sentence ):
    str = ''
    for c in sentence : # 해당 문장을 문자 하나씩 c 대입
        # if c != '.' or c != ' ':  # 문자가 . 아니거나 공백이 아니면 비교
        if c != '.' and c != ' ' :  # 문자가 . 아니면서 공백도 아니면 비교
            str += c                # str 에 문자 저장
    size = len(str)                 # 합쳐진 문자 길이 구하기
    for i in range( size // 2 ) :   #   // : 몫   문자길이//2
        if str[i] != str[size -1 - i]: # 첫문자 와 마지막문자가 다를경우
            return False                # 팰린드롬 x
    return True # 팰린드롬 o

sentence1 = "never odd or even."
ret1 = solution( sentence1 )
print("solution1 함수 결과 " , ret1)

sentence2 = "palindrome"
ret2 = solution( sentence2 )
print("solution2 함수 결과 " , ret2)
