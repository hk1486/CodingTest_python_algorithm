
import sys
#sys.stdin=open("input.txt","rt")

n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

for i in range(len(b)):
    a.append(b[i])

for _ in sorted(a):
    print(_, end = ' ')
