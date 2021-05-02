
# 문제 21 : 인덱싱 [문자순서] : 0번시작
letters = 'python'
print( letters[0]  , letters[2] )

# 문제 22 : 슬라이싱[ 시작번호 , 끝번호 , 단위 ]
    # 시작번호부터 끝번호 전까지의 문자 출력
license_plate = "24가 2210"
print( license_plate[-4:] ) # 뒤에서부터 4개
print( license_plate[4:8] )

# 문제 23 :
string ="홀짝홀짝홀짝"
print( string[ 0 : 6 : 2 ]) # 0부터 6전까지 2단위로 이동  [ 0 2 4 ]

# 문제 24 : 슬라이싱 반대로
string = "PYTHON"
print( string[  :  : -1 ]) # 뒤에부터 시작

# 문제 25 : replace( "기존문자" , "새로운문자" ) 교체 함수
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace( "-" , " ") # -(하이픈)을 공백으로 치환
print( phone_number1 )

# 문제 26 : 문제25 모두 붙여서 출력
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace( "-" , "")
print( phone_number1 )

# 문제 27 : split() : 분리[분열] 함수
url = "http://sharebook.kr"
url_split = url.split(".") # .[점] 기준으로 자르기
print( url_split[1] )

# 문제28 : 예상 : 오류 발생  !!:이유
# lang = "python"
# lang[0] = 'P' # 이유 : 문자열 일부분 수정 불가
# print(lang)

# 문제29 :  replace  교체함수
string = "abcdfe2a354a32a"
string = string.replace( "a" , "A")
                        #기존  #새로운
print(string)

# 문제30 : 예상 abcd => aBcd 교체 된다











