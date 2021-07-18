def func_a(current_grade, last_grade, rank, max_diff_grade): # 장학생 구하기 함수
    arr_length = len(current_grade) # 전체 학생수
    count = 0 # 장학생수
    for i in range(arr_length): # 전체 학생수 만큼 반복
        if current_grade[i] >= 80 and rank[i] <= arr_length // 10:
            # 이번학기의점수가 80점이상 이면서 (전체학생수//10) : 상위 10%위내 이면
            count += 1 # 장학생수 증가
        elif current_grade[i] >= 80 and rank[i] == 1:
            # 이번학기의점수가 80점이상 이면서 순위가 1등이면
            count += 1 # 장학생수 증가
        elif max_diff_grade > 0 and max_diff_grade == current_grade[i] - last_grade[i]:
            # 최대값이 0보다 크고 최대값이 이번학기-직전학기  같으면
            count += 1 # 장학생수 증가
    return count

def func_b(current_grade): # 석차 구하는 함수
    arr_length = len(current_grade) # Len( 리스트 ) : 리스트내 요소들의 개수
    rank = [1] * arr_length
    for i in range(arr_length): # 학생수[i] 만큼 반복
        for j in range(arr_length): # 학생수[j] 만큼 반복
            if current_grade[i] < current_grade[j]:
                # 이번학기[i] < 이번학기[j]
                rank[i] += 1 # 더 작으면 순위 내리기
    return rank
    # i = 0     j = 0   j=1  j=2  j=3  j=4 j=5
    # i 1증가 할때마다 j는 5번씩 실행
def func_c(current_grade, last_grade): #이번학기 와 직전하기의 최대값
    max_diff_grade = 1 # 최대값 변수
    for i in range(len(current_grade)):
        max_diff_grade = max(max_diff_grade, current_grade[i] - last_grade[i])
        # max( 현재최대값 , (이번학기-직전학기) )
    return max_diff_grade

def solution(current_grade, last_grade):
    rank = func_b(current_grade) # 이번학기의 순위 구하기
    max_diff_grade = func_c(current_grade , last_grade) # 이번학기와 직전학기 이용한 최대값
    answer = func_a( current_grade , last_grade , rank , max_diff_grade ) #장학생수 구하기
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
current_grade = [70, 100, 70, 80, 50, 95] # 이번 학기
last_grade = [35, 65, 80, 50, 20, 60] # 직전 학기
ret = solution(current_grade, last_grade)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret, "입니다.")