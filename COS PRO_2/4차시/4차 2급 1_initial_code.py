def solution(schedule): # 상담을 받지 못한[X] 학생수 찾는 함수
    answer = [] # 상담을 받지 못한 학생 리스트
    for idx, i in enumerate(schedule):
        # idx : 리스트내 요소 번호
        # i : 리스트내 요소 값
        #  for 인덱스번호 , 값 enumerate( 리스트 )
            # 값이 x이면 answer(결과) 리스트에  요소번호를 저장
        if i == 'X': #  i 가 X 이면 상담을 못받음
            answer.append( idx+1 ) # x를 받은 학생의 번호를 저장
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
schedule = ["O", "X", "X", "O", "O", "O", "X", "O", "X", "X"] # 스케줄 매개변수
ret = solution(schedule) # 함수 호출

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")