#문제5
def solution(arr):
    left, right = 0, len(arr)-1
    #왼쪽=0   오른쪽 =0   숫자갯수
    while left < right : # 오른쪽이 더 클 경우에만
        arr[left], arr[right] = arr[right], arr[left]
            #리스트[왼] , 리스트[오른쪽] = 리스트[오른쪽] , 리스트[왼]
        left += 1 # 왼쪽 1 증가
        right -= 1 # 오른쪽 1 감소
    return arr

arr = [1, 4, 2, 3]
ret = solution(arr)

print("Solution: return value of the function is ", ret, " .")
