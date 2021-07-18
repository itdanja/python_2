
# 문제 151 : 0 보다 작은수 만 출력
리스트 = [ 3 , -20 , -3 , 44 ]
for 변수 in 리스트 :
    if 변수 < 0 : # 만약에 변수가 0보다 작으면
        print( 변수 ) # 출력
    # 아니면 생략

# 문제 152 : if 와 for문
리스트 = [ 3 , 100 , 23 , 44 ]
for 변수 in 리스트 :
    if 변수 % 3 == 0 : # 만약에 변수가 % 3 했을때 나머지가 0 이면
        print( 변수 )
    # 아니면 출력

# 문제 153 : if 와 for문
리스트 = [ 13 , 21 ,12 , 14 ,30 ,18]
for 변수 in 리스트 :
    if 변수 < 20 and 변수 % 3 == 0 :
        print( 변수 )

# 문제 154 : 세글자 이상의 문자를 출력
리스트 = ["I" , "study" , "python" , "language" ,"!"]
for 변수 in 리스트 :
    if len( 변수 ) >= 3 : # 만약에 글자수가 3글자이상이면
        print( 변수 )

# 문제 155 : isupper()
리스트 = ["A" , "b" , "c" , "D"]
for 변수 in 리스트 :
    if 변수.isupper() : # 만약에 변수가 대문자 이면
        print( 변수 )

# 문제 156
리스트 = ["A", "b", "c", "D"]
for 변수 in 리스트 :
    if 변수.islower() :
        print( 변수 )

# 문제 157 : capitalize() 첫글자만 대문자로 변환 함수
리스트 = ["dog" , "cat" , "parrot"]
for 변수 in 리스트 :
    print( 변수.capitalize())

# 문제 158 : split() 분리 함수
리스트 = ["hello.py" , "ex01.py" , "intro.hwp"]
for 변수 in 리스트 :
    분리 = 변수.split(".")   #  . 기준으로 분리
    print( 분리[0] ) # 분리 기준으로 앞문자 출력

# 문제 159 : split() 분리 함수
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트 :
    분리 = 변수.split(".") # . 기준으로 분리
    if 분리[1] == "h" : # 분리 기준으로 2번째 문자 비교
        print( 변수 )

# 문제 160
리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
for 변수 in 리스트 :
    분리 = 변수.split(".") # . 기준으로 분리
    if 분리[1] == "h" or 분리[1] == "c" : # 분리 기준으로 2번째 문자 비교
        print( 변수 )
























