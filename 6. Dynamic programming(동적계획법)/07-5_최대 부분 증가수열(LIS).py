import sys
sys.stdin = open("input.txt",'r')

n = int(input())
a = list(map(int,input().split()))
a.insert(0,0)
dy = [0]*(n+1)
dy[1] = 1
res = 0

for i in range(2,n+1): # 1번째 인덱스는 1이니까 2번째 인덱스부터
    max = 0 # 맥스값 초기화
    for j in range(i-1, 0, -1): # 현위치에서 전값부터 1번째 인덱스까지 비교해보면서
        if a[j] < a[i] and dy[j]>max: # 현위치값이 전위치 값보다 크고 dy배열의 전위치 값이 맥스값보다 크면
            max=dy[j] # 맥스값은 dy배열의 전위치의 값
    dy[i] = max+1 # 한번 다찾고 난 뒤 가장 큰값에서 +1 한것을 dy배열의 현위치에 저장
    if dy[i] > res: # 전체적으로 돌면서 최대값 찾음
        res = dy[i]
print(res)

