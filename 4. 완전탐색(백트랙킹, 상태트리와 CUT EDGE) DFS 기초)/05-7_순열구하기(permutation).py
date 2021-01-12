import sys
#sys.stdin = open("input.txt", "r")
from itertools import permutations

n, m = map(int,input().split())
data = [i for i in range(1,n+1)]
res = list(permutations(data,m))

for i in res:
    print(str(i).strip('()').replace(',',''))
print(len(res))

