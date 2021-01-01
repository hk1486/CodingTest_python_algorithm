import sys
#sys.stdin=open("input", "r")
n, m = map(int,input().split())
a = list(map(int,input().split()))

a.sort()
for i in range(n):
    if a[i] == m:
        print(i+1)
