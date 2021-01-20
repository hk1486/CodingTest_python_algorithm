import sys
sys.stdin=open("input.txt", "r")
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

def DFS(x, y):
    global cnt
    cnt+=1 # 집을 찾을때마다 +1
    board[x][y]=0 # 찾으면 0으로 바꿔줌
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<n and board[xx][yy]==1:
            DFS(xx, yy)

if __name__=="__main__":
    n=int(input())
    board=[list(map(int, input())) for _ in range(n)]
    res=[] # 단지 개수 추가하는 배열
    for i in range(n): # 2중 for문 돌면서 4방향탐색으로 못찾을때까지 탐색
        for j in range(n):
            if board[i][j]==1:
                cnt=0 # 단지마다 cnt=0으로 초기화
                DFS(i, j)
                res.append(cnt)
    print(len(res))
    res.sort()
    for x in res:
        print(x)