# 문제1 : 리스트내 동일한 개수 세기
    # 조건 1: 리스트에 사이즈별로 개수를 담아서 리턴해주는 함수

def 함수(선호티셔츠):  #함수 만들기
    티셔츠개수 = [ 0 , 0 , 0 , 0 , 0 , 0 ] # 처음에는 0으로 설정
                #XS  #S  #M  #L  #XL #XXL
    for 티셔츠 in 선호티셔츠 : # 선호티셔츠 하나씩 티셔츠에 넣기
        if 티셔츠 == "XS" :    # 만약에 "XS" 이면
            티셔츠개수[0] += 1     # XS 자리에 1 추가
        if 티셔츠 == "S" :     # 만약에 'S' 이면
            티셔츠개수[1] += 1     # S 인덱스에 1추가
        if 티셔츠 == "M" :
            티셔츠개수[2] += 1
        if 티셔츠 == "L" :
            티셔츠개수[3] += 1
        if 티셔츠 == "XL" :
            티셔츠개수[4] += 1
        if 티셔츠 == "XXL" :
            티셔츠개수[5] += 1

    return 티셔츠개수  # 함수 끝내기 => 티셔츠 개수 반환
# 학생들이 선호하는 티셔츠 목록
선호티셔츠 = [ "S" , "S" , "XS" , "L" , "XXL", "S" , "XL" , "L"]
    # XS = 1    S = 3    M = 0   L = 2   XL = 1  XXL = 1

print( "함수 실행 결과 : " ,  함수(선호티셔츠) )  # 함수 호출하기

############################################################################################################

def 초등학생세기( 학생나이목록 ):

    초등학생인원수 = [ 0 , 0, 0, 0, 0, 0 ]

    for 초등학생 in 학생나이목록 :
        if 초등학생 == 8 :      # 1학년 이면
            초등학생인원수[0] += 1
        if 초등학생 == 9 :      # 2학년 이면
            초등학생인원수[1] += 1
        if 초등학생 == 10 :     # 3학년 이면
            초등학생인원수[2] += 1
        if 초등학생 == 11 :     # 4학년 이면
            초등학생인원수[3] += 1
        if 초등학생 == 12 :     # 5학년 이면
            초등학생인원수[4] += 1
        if 초등학생 == 13 :     # 6학년 이면
            초등학생인원수[5] += 1
    return 초등학생인원수

# 학생들의 학년별[초등학생] 인원세기
학생나이목록 = [ 8 , 8 , 9 , 10 , 10 ,10 , 11 , 9 , 8 , 12 , 13 , 8 , 11 ]
print("초등학생의 인원수 : " , 초등학생세기( 학생나이목록) )

#####################################################################################################################
# 문제 만들기

