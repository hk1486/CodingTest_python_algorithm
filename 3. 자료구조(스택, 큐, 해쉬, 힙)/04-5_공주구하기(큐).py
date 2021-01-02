import sys
#sys.stdin=open("input", "r")
from collections import deque

n, k = map(int,input().split())
dq = list(range(1, n+1)) #  1~n까지
dq = deque(dq) # 큐 만들어주기(데크)

while dq: # 큐가 비면 멈춤
    for _ in range(k-1): # k번째 전까지 pop해주고 뒤에 append
        a = dq.popleft()
        dq.append(a)
    dq.popleft() # k번째 사람 pop
    if len(dq) == 1: # 한명만 남았을때
        print(dq[0])
        dq.popleft()

