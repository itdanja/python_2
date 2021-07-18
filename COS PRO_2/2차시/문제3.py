
#문제3

import math

def solution( N , M ):
    total = 0
    for x in range( N , M+1 ) :
                # 4부터 8 전까지 1씩 증가
        if x % 2 == 0 :
            # ==0 짝수     == 1 홀수
            total += x*x
            # 수*수 = 제곱
    return total

N = 4  # 4 5[홀X] 6[짝] 7[홅]
M = 7
    # 4*4 = 16     6*6 = 36    => 52
ret = solution( N , M )
print("solution 함수의 결과 : ", ret )
