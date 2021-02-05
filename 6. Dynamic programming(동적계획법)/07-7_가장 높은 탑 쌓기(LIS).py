import sys
sys.stdin = open("input.txt",'r')

n = int(input())
lst = [tuple(map(int,input().split())) for _ in range(n)]
lst.sort(reverse=True)
dy = [0]*(n+1) # 모든 경우의 수를 넣는 다이나믹리스트 하나 만들기
dy[0] = lst[0][1]
res = lst[0][1] # 초기화

for i in range(1,n):
    max_h = 0
    for j in range(i-1,-1,-1): # i번째 벽돌 바로 밑의 벽돌을 찾음
        if lst[i][2] < lst[j][2] and dy[j] > max_h: # 쌓을 수 있을때,
            max_h = dy[j] # j번째 벽돌이 가장 상단이면서 그 탑의 최대 높이를 맥스에 기록
    dy[i] = max_h + lst[i][1] # j번째 벽돌에 i번째 벽돌을 올리니까 그 값을 더해줌
    res = max(res, dy[i]) # 그 중에 가장 높은 높이 찾기
print(res)