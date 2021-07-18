
#문제4 : 글자길이가 5 이상인 단어를 이어 출력하기
    # len( 문자 ) : 문자의 길이
def solution( 단어목록 ):
    결과 =""
    for 단어 in 단어목록 : # 단어목록내 단어를 하나씩 단어에 대입 반복
        if len(단어) >= 5 : # 단어길이가 5 이상이면
            결과 += 단어    # 결과에 단어 추가
    if len(결과) < 1 :    # 결과에 아무 단어가 없으면
        결과 ="empty"        # empty 넣기
    return 결과

단어목록1 = [ "my" , "favorite" , "color" , "is" , "violet"]
print( " 5글자 이상인 단어 합치기 결과 : " , solution(단어목록1) )

단어목록2 = ["yes" , "i" , "am"]
print( " 5글자 이상인 단어 합치기 결과 : " , solution(단어목록2) )
