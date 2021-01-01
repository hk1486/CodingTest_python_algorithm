
import sys
# sys.stdin=open("input.txt","rt")

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
res = 0

s = e = n//2 # for 문 범위를 지정해주기 위해
for i in range(n):
    for j in range(s , e+1): # s부터 e까지
        res += a[i][j]
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(res)