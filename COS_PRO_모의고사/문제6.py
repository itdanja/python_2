#문제6
    # 단어가 단어목록에서 오타의 개수 구하기
    # zip( 단어1 , 단어2 )
        # ( 단어1 첫글자 , 단어2 첫글자 )
        # ( 단어1 두번째 글자 , 단어2 두번째 글자 )
        # ( 단어1 세번째 글자 , 단어2 세번째 글자 )
        # ( 단어1 네번째 글자 , 단어2 네번째 글자 )

def solution( 단어목록 ) :
    오타수 = 0
    for 오타단어 in 단어목록 : # 단어목록 리스트에서 하나씩 오타단어에 대입
        for x , y in zip( 오타단어 , 단어 ) :
            if x != y : # x[오타단어의 1~4번째 문자] 와 y[ 단어의 1~4번째 문자] 다르면
                오타수 += 1 # 오타수 1 증가
    return 오타수

단어목록 = ["CODE" , "COED" , "CDEO"]
단어 = "CODE"
print(" 오타의 개수 : " , solution(단어목록) )
