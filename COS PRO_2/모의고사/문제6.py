
# k 의 키보다 더 큰 키의 인원수 구하기

def solution(height, k):
    answer = 0          # k보다 큰 수의 개수
    n = len(height)     # 키의 목록 개수
    for h in height:       # 키 리스트를 하나씩 h에 대입
        if h > k:          #  h가 k보다 더 크면
        #   >= 이상   ->   > 초과
            answer += 1     # k보다 큰 수의 변수에 +1
    return answer