
# 리스트에 들어있는 값만큼 인덱스 뛰기
def solution(stones): # stones : 징검다리에 적혀있는 수 의 리스트
    cnt = 0             # 점프한 개수
    current = 0         # 현재 개구리의 위치
    n = len(stones)     # 징검다리 개수  = len(리스트)
    while current < n : # 현재위치가 징검다리 개수 작으면 반복실행
        # 현재위치가 마지막징검다리 까지 반복
        current += stones[current]
        # 개구리 현재 위치에 더해주기 [ 징검다리에 적혀있는 수를  ]
        cnt += 1 # 점프수 증가
    return cnt # 점프수 반환

