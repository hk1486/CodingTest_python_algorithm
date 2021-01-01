
import sys
#sys.stdin=open("input.txt","rt")
dx = [-1,0,1,0] # 탐색을 위해 행을 이동하기 위한 배열(상,우,하,좌)(시계방향)
dy = [0,1,0,-1] # 탐색을 위해 열을 이동하기 위한 배열(상,우,하,좌)(시계방향)

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
a.insert(0,[0]*n) # 위 가장가지 0으로 초기화
a.append([0]*n) # 아래 가장자리 0으로 초기화
for x in a:
    x.insert(0, 0) # 한 행 앞부분 0으로 초기화
    x.append(0) # 한 행 뒷부분 0으로 초기화
cnt = 0
 
for i in range(1,n+1): # 행 번호 1부터 시작
    for j in range(1,n+1): # 열 번호 1부터 시작
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)): # *all() : if절에서 조건이 모두 참일때 실행 
            cnt += 1
print(cnt)
