
# 거스름돈을 구하기
    # 지불한 금액 - 총 구매한 가격

def solution(price, money):
    #price : 구매한 가격들의 리스트
    #money : 지불한 금액
    answer = money - sum(price)
        # sum( 리스트 ) : 리스트내 요소들의 전체 합계
    # answer : 거스름돈

    # 만약에 지불한 금액보다 구매할 총구매금액 더 크면
    if answer < 0 : # 만약에 거스름돈이 마이너스이면
        answer = -1 # -1 리턴
    return answer
