import sys
#sys.stdin = open("input.txt",'r')

n, m = map(int,input().split())
s = []
t = []
lst = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    s.append(lst[i][0])
    t.append(lst[i][1])
dy = [0]*(m+1)

for i in range(n):
    for j in range(m,t[i]-1,-1):
        dy[j] = max(dy[j], dy[j-t[i]]+s[i])

print(dy[m])