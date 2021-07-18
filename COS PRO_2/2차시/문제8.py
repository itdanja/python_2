
#문제8 : 각 자릿수별 소수구하기 => 한줄 변경
def solution( number ) :
    count = 0  # 자연수의 개수
    #while number >=0 :
    while number : #  정수가 있을때까지 반복  # !!!!!: 정답으로 수정
        n = number % 10 # 끝 한자리 구하기
        if n ==2 or n == 3 or n == 5 or n == 7 :
            # 끝 한자리가 2 , 3 , 5 , 7 이면  자연수
            count +=1 # 자연수 개수 증가
        number //=10 # 나머지 버리기
    return count


number = 29022531  #   29022531 % 10 => 1
#   2902253 % 10 => 3
#   290225 % 10 => 5
ret = solution( number )

print(" solution 실행 결과 값은 : " , ret )