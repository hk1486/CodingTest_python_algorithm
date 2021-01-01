
import sys
#sys.stdin=open("input.txt","rt")

n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
m = int(input())
for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0:
        for _ in range(k): # k만큼 회전
            a[h-1].append(a[h-1].pop(0)) # 0번째꺼pop한후 뒤 남는자리에 append
    else:
        for _ in range(k): # k만큼 회전
            a[h-1].insert(0, a[h-1].pop()) # 맨뒤꺼pop한후 0번째에 insert
s = 0
e = n
res = 0
for i in range(n):
    for j in range(s,e):
        res += a[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(res)
    
