import sys

n = int(sys.stdin.readline())   #기타 개수 n 입력
s = [input() for i in range(n)]    #시리얼 번호 n개 입력

#정렬 2_자릿수 합
def sum(x):
    r = 0
    for i in x:
        if i.isdigit():     #isdigit(): 문자열이 숫자인지 판별
            r += int (i)
    return r

#정렬_ 1.길이 2.자릿수 합 3.사전순
s.sort(key = lambda x: (len(x), sum(x), x))

#정렬된 리스트 s의 모든 요소 출력
for i in s:
   print(i)



