def solution(name_list):
        # name_list : 학생들의 이름목록 
    answer = 0      #이름에 j , k 포함되어있는 학생수
    for name in name_list: # 학생목록에 하나씩 name에 대입
        for n in name: # name에 문자 하나씩 n에 대입
            if n == 'j' or n == 'k':
                # 해당 문자가 j 또는 k 이면
                answer += 1 # 구하는학생수에 +1
                # continue # 가장 가까운 반목문으로 이동
                # j 또는 k을 찾았으면 다시 학생이름 으로 이동
                break

    # continue : 가장 가까운 for 다시 실행
    # break : 가장 가까운 for 종료

    return answer