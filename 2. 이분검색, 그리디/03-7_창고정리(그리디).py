import sys
#sys.stdin=open("input", "r")

n = int(input())
lst = list(map(int,input().split()))
m = int(input())
lst.sort()

for _ in range(m):
    lst[0] += 1
    lst[n-1] -= 1
    lst.sort()
print(lst[n-1]-lst[0])



