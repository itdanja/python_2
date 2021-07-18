

def solution(scores):
    grade_counter = [0 for i in range(5)]
        # grade_counter : 학점목록에 학점[A~F] 5개을 0으로 설정

    for x in scores: # 점수목록에서 하나씩 X에 대입
        if x >=85 : # x가 85점 이상이면
            grade_counter[0] += 1       # 학점목록[0] = A학점 한명 추가
        elif x >=70  : # x가 70점 이상이면
            grade_counter[1] += 1       # 학점목록[1] = B학점 한명 추가
        elif x >=55: # x가 55점 이상이면
            grade_counter[2] += 1       # 학점목록[2] = C학점 한명 추가
        elif x >=44 : # x가 44점 이상이면
            grade_counter[3] += 1       # 학점목록[3] = D학점 한명 추가
        else:   # 그외
            grade_counter[4] += 1       # 학점목록[4] = F학점 한명 추가

    return grade_counter
