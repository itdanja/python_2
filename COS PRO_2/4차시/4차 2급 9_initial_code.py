#다음과 같이 import를 사용할 수 있습니다.
#import math
def solution(height):
    count = 0  # 위험지역 총 개수
    dx = [ -1 , 1 , 0 , 0 ]
    dy = [ 0 , 0 , -1 , 1 ]
    for i in range(4) :  # 4번 반복
        for j in range(4) : # 4번 반복
            위험지역 = True
            for k in range(4) : # 4번 반복
                if 0<= i+dx[k] and i+dx[k] < 4 and 0 <= j+dy[k] and j+dy[k]<4 :
                    if height[ i+dx[k]][j+dy[k]] <= height[i][j] :
                        위험지역 = False
            if 위험지역 :
                count += 1
    return count

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
height = [
    [3, 6, 2, 8],
    [7, 3, 4, 2],
    [8, 6, 7, 3],
    [5, 3, 2, 9] ]
# 현재 수 기준으로 오른쪽[동] 왼쪽[서] 아래[남] 위[북] 수 가 현재 수보다 더 클경우 위험지역
# 2차원리스트 [ [첫번째줄] , [두번째줄] , [세번째줄] , [네번째줄 ] ]

ret = solution(height)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")