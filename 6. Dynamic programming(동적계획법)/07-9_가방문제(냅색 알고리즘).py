import sys
#sys.stdin = open("input.txt",'r')

n, m = map(int,input().split())
jew = [tuple(map(int,input().split())) for _ in range(n)]
dy = [0]*(m+1)
w = []
v = []

for i in range(n):
    w.append(jew[i][0])
    v.append(jew[i][1])

for i in range(n):
    for j in range(w[i],m+1):
        dy[j] = max(dy[j], dy[j-w[i]] + v[i])

print(dy[m])