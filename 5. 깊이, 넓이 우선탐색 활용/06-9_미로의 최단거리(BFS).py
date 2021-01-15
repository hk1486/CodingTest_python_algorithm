import sys
sys.stdin = open("input.txt", "r")
from collections import deque

dx = [-1,0,1,0]
dy = [0,1,0,-1]

a = [list(map(int,input().split())) for _ in range(7)]
a[0][0] = 1

ch = [[0]*7 for _ in range(7)]

Q = deque()
Q.append((0,0))

while Q:
    tmp = Q.popleft()
    for i in range(4):
        x = tmp[0] + dx[i]
        y = tmp[1] + dy[i]
        if 0<=x<=6 and 0<=y<=6 and a[x][y] == 0: # 경계선 범위내에 있고, 갈 수 있는 길(0)일때.
            a[x][y]=1 # 1로 바꿈으로써 최단거리 찾기 가능
            ch[x][y] = ch[tmp[0]][tmp[1]] + 1
            Q.append((x,y))
if ch[6][6] == 0:
    print(-1)
else:
    print(ch[6][6])