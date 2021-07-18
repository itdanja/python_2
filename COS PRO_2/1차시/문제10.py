
#문제10 : 평균보다 작은 수가 몇개인지 출력하는 함수
def solution( data ):
    total = sum(data)       # 총점수 합계
    #average = len(data) / total   # 갯수 / 합계
    average = total / len(data )   # 평균  = 합계 / 갯수
    cnt = 0
    for d in data :
        if d <= average :
            cnt += 1
    return cnt

data1 = [ 1 ,2 ,3 ,4 ,5 ,6 ,7 , 8 , 9 , 10]
ret1 = solution(data1)
print("solution1 함수 결과 " , ret1)

data2 = [ 1,1,1,1,1,1,1,1,1,10 ]
ret2 = solution(data2)
print("solution2 함수 결과 " , ret2)

