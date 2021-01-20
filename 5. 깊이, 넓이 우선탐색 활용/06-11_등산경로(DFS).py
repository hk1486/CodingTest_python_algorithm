import sys
sys.stdin = open("input.txt", "r")

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def DFS(x,y):
    global cnt
    if x == x1 and y == y1:
        cnt += 1
    else:
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<=(n-1) and 0<=yy<=(n-1) and a[xx][yy] > a[x][y]:
                DFS(xx,yy)

if __name__ == "__main__":
    n = int(input())
    a = [list(map(int,input().split())) for _ in range(n)]
    cnt = 0
    MAX = max(map(max,a)) # 2차원 배열에서 최대값 찾기
    MIN = min(map(min,a)) # 2차원 배열에서 최소값 찾기
    for i in range(n):
        for j in range(n):
            if a[i][j] == MAX: # 도착점일때 주소값 저장
                x1, y1 = i, j
            if a[i][j] == MIN: # 출발점일때 주소값 저장
                x2, y2 = i, j
    DFS(x2,y2) # 출발점 주소값
    print(cnt)
