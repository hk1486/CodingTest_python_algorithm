import sys
#sys.stdin = open("input.txt", "r")
from itertools import product
import re

n, m = map(int,input().split())
data = [_ for _ in range(1,n+1)]
result = list(product(data,repeat=m))

for i in result:
    a = str(i).strip('(,)').replace(',','')
    print(a)
print(len(result))





