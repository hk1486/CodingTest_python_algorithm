import sys
sys.stdin = open("input.txt", "r")

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def DFS(x,y):
    global cnt
    if x == 6 and y == 6:
        cnt += 1
    else:
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<=6 and 0<=yy<=6 and a[xx][yy] == 0:
                a[xx][yy] = 1
                DFS(xx,yy)
                a[xx][yy] = 0 # 뒤로 백할때 0으로 다시 바꿔줘야 다른길 찾을 수 있음

if __name__ == "__main__":
    a = [list(map(int,input().split())) for _ in range(7)]
    a[0][0] = 1
    cnt = 0
    DFS(0,0) # 시작점
    print(cnt)
