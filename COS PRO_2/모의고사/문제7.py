
# a -> z   z->a      변경하기
def solution(s):
        # s : 문자 abz
    s_lst = list(s)
    n = len(s)          # n = 문자열 개수
    for i in range(n):     # 문자열 개수 반복
        if s_lst[i] == 'a': #만약에 리스트에[i] == 'a' 이면
            s_lst[i] = 'z'  # z 로 변경
        # if s_lst[i] == 'z':
        elif s_lst[i] == 'z': #만약에 리스트에[i] == 'z' 이면
            s_lst[i] =  'a' # a로 변경

    # 첫번째 IF가 T 이더라도 두번째 IF도 검사 실행
    # if 조건1 :
    # if 조건2 :

    # 첫번째 IF가 T 이면 두번째 elif는 검사 안함
    # if 조건1 :
    # elif 조건2 :

    return "".join(s_lst) # "" 뒤에 문자열 붙이기