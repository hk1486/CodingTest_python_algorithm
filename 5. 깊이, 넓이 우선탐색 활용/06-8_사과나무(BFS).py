import sys
sys.stdin = open("input.txt", "r")
from collections import deque

dx = [-1,0,1,0] # x축 이동위해 12,3,6,9시 방향
dy = [0,1,0,-1] # y축 이동위해 12,3,6,9시 방향

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]

ch = [[0]*n for _ in range(n)] # 2차원 체크리스트 배열
ch[n//2][n//2] = 1 # 정가운데부터 탐색하기위해 그 값을 체크

sum = 0
sum += a[n//2][n//2] # 해당 정가운데값 더해줌

Q = deque()
Q.append((n//2, n//2)) # 데크에 정가운데값 추가

L = 0 # 레벨은 0부터
while True:
    if L == n//2:
        break
    size = len(Q)
    for i in range(size): # 큐의 사이즈만큼 돈다.
        tmp = Q.popleft() # 하나 팝한거에서 상하좌우로 가지 뻗는다.
        for j in range(4): # 4방향 탐색
            x = tmp[0]+dx[j]
            y = tmp[1]+dy[j]
            if ch[x][y] == 0: # 체크리스트에서 x,y좌표가 0일때만
                sum+=a[x][y] # 값을 더해줌
                ch[x][y]=1 # 다시 1로 체크해줌
                Q.append((x,y)) # 그 좌표를 다음 탐색을 위해 데크에 넣음
    L += 1  # for문이 끝났을때, 탐색이 끝났으므로 레벨 증가
print(sum)