import sys

t = int(sys.stdin.readline())                               # 테스트 케이스 개수 t

for i in range (t):
    n, m = map(int, input().split())
    queue = list(map(int, input().split()))                 # 리스트 queue
    cnt = 0                                                 # 문서의 출력 순서를 세기 위한 변수 cnt

    while queue:
        if queue[0] == max(queue):                          # 맨 앞 문서의 중요도가 가장 클 때
            del queue[0]                                    # 맨 앞 문서 삭제
            m -= 1                                          # 문서 위치 왼쪽으로 한 번 이동하므로 m 값 1 감소
            cnt +=1                                          # 문서 하나 출력 되었으므로 cnt 값 1 증가
        else:                                                   # 맨 앞 문서의 중요도가 가장 크지 않을 때
            queue.append(queue[0])                              # 이 문서를 맨 뒤에 추가  
            del queue[0]                                        # 맨 앞에서 삭제

            if m == 0:                                          # m이 0일 경우
                m = len(queue)-1                                # m 맨 뒤 가리킴
            else:                                               # m이 0이 아닐 경우
                m -= 1                                          # m 값 1 감소
    
    print(cnt)                                                 # cnt 값 출력