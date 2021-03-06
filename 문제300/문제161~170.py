
# 문제 161 : range( ) : 범위함수
for 변수 in range(100) :
    print( 변수 )

# 문제 162 : 4씩 증가하기
for 변수 in range( 2002 , 2051 , 4 ) :
    print( 변수 )

# 문제 163 : 1~30까지 중 3의 배수
for 변수 in range( 3 , 31 , 3 ) :  # 3부터 30까지 3씩 증가
    print( 변수 )

# 문제 164 : 99 부터 0까지 1씩 감소
for 변수 in range(100) :
    print( 99 - 변수 )
            ## 99 - 0    99 - 1   99 - 2  99 - 3  ~~~  99 - 99

# 문제 165
for 변수 in range(10) : # 0부터 9까지 1씩 증가
    print( 변수 / 10  )

# 문제 166 : 구구단 3단
for 곱 in range( 1 , 10) :
    print( 3 , "X" , 곱 , "=" , 3*곱 )

# 문제 167 : 3단 홀수만
for 곱 in range(1, 10):
    if 곱 % 2 == 1 :
        print(3, "X", 곱, "=", 3 * 곱)

# 홀수 / 짝수 구하기
#   값 % 2 == 0  : 해당 값은 짝수
#   값 % 2 == 1  : 해당 값은 홀수
# 배수 구하기
#   값 % 수 == 0  : 나머지가 0 이면 값은 그의 수의 배수

# 문제 168 : 1~10까지의 숫자를 모두 더한 값 [ 누적합계 ]
합계 = 0
for 변수 in range( 1 , 11 ) :
    합계 += 변수  # 합계변수에 변수를 더한 후에 합계변수에 대입

print( "누적합계 : " , 합계 )

# 문제 169 :
합계 = 0
for 변수 in range( 1 , 11 ) :
    if 변수 % 2 == 1 :  # 홀수 구하기
        합계 += 변수  # 합계변수에 변수를 더한 후에 합계변수에 대입

print( "홀수 누적합계 : " , 합계 )

# 문제 170
누적곱 = 1 # 곱하기를 하기 때문에 0으로 시작할수 없음
for 변수 in range( 1 , 11 ) :
    누적곱 *= 변수  # 합계변수에 변수를 곱한 후에 누적곱 변수에 대입

print( "누적곱 : " , 누적곱 )
















