import sys
#sys.stdin = open("input.txt",'r')

n = int(input())
coin = list(map(int,input().split()))
money = int(input())
dy = [10000]*(money+1) # 그냥 넉넉한 값으로 배열 값을 잡아줌, min쓰기위해
dy[0] = 0 # 0번째 인덱스 0으로 초기화 필수 (어차피 0원이면 거슬러주는 돈도 0개)

for i in range(n):
    for j in range(coin[i],money+1):
        dy[j] = min(dy[j], dy[j-coin[i]]+1)

print(dy[money])

