
#문제6 # @@@ 빈칸채우기
def solution(floors):
    dist = 0
    length = len(floors)  # 리스트내 층 개수 : 5
    for i in range( 1 , length ):  # 1 ~ 5전까지
        if floors[i] > floors[i-1]: # 현재층과 앞전층 비교했을때
            # 현재층이 더 크면
            dist += floors[i] - floors[i-1]
        else:
            # 앞전층이 더 크면
            dist += floors[i-1] - floors[i]
    return dist
        #  층 [ 1 , 2 , 5 , 4 ,2 ]
            #  2 > 1
                #    2-1  =>  dist  = 1
            # 5 > 2
                #   5-2  =>  dist = 3
            # 4 > 5 [x]
                #   5-4  => dist = 1
            # 2 > 4 [ x]
                #   4-2  => dist = 2


floors = [1, 2, 5, 4, 2] # 하루 동안 엘리베이터가 멈춘 층
        # 층과 층 사이의 거리는 1
        # 1 -> 2  [ 1 ]
        # 2 -> 5  [ 3 ]
        # 5 -> 4  [ 1 ]
        # 4 -> 2  [ 2 ] => 총 : 7
ret = solution(floors)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")