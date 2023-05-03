import sys
input = sys.stdin.readline

n = int(input()) # 입력할 좌표 수 : 2차원 배열의 크기

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merged_arr = []
    l = r = 0

    while l < len(left) and r < len(right):
        # x 좌표가 같을 경우 : y좌표를 비교해서 작은 값 리스트에 넣기
        #[][0] : x좌표, [][1] : y좌표인 2차원 배열
        if left[l][0] == right[r][0]:
            if left[l][1] < right[r][1]:
                merged_arr.append(left[l])
                l += 1
            else:
                merged_arr.append(right[r])
                r += 1
        elif left[l][0] < right[r][0]:
            merged_arr.append(left[l])
            l += 1
        else:
            merged_arr.append(right[r])
            r += 1
    
    merged_arr += left[l:]
    merged_arr += right[r:]

    return merged_arr

# 입력받은 문자열 n개의 행을 int형 2차원 리스트로 변환-> a에 할당
a = [list(map(int,input().split())) for i in range(n)]
a = merge_sort(a)

for i in a:
    print(i[0],i[1])