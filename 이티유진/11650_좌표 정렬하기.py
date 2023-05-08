import sys

n = int(sys.stdin.readline())   #n 입력

arr = [list(map(int,input().split())) for i in range(n)]    #2차원 평면 위의 점 n개 입력 [[3,4],[1,1]]

#병합정렬_merge
def merge(left, right):
        i, j = 0, 0
        sorted_list = []
        while(i < len(left)) and (j < len(right)):
            if left[i] < right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1
        if i == len(left):
             while j < len(right):
                  sorted_list.append(right[j])
                  j += 1
        elif j == len(right):
             while i < len(left):
                  sorted_list.append(left[i])
                  i += 1
        return sorted_list

#병합정렬_merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    #분할하고 분할된 리스트 각각 정렬
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    #병합
    return merge(left,right)

#정렬
arr = merge_sort(arr)
#좌표 출력
for x, y in arr:
     print(x,y)


