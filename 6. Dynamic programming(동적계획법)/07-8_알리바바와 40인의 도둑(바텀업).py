import sys
sys.stdin = open("input.txt",'r')

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
dy = [[0]*n for _ in range(n)]
dy[0][0] = lst[0][0] # 0번째 값 초기화

for i in range(1,n): # 행과 열 첫 줄 채우기
    dy[0][i] = dy[0][i-1] + lst[0][i]
    dy[i][0] = dy[i-1][0] + lst[i][0]

for i in range(1,n): # 최소값으로 나머지 채우기
    for j in range(1,n):
        dy[i][j] = min(dy[i-1][j], dy[i][j-1]) + lst[i][j]

print(dy[n-1][n-1])
