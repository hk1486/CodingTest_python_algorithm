import sys
#sys.stdin=open("input", "r")
from collections import deque

a = input()
n = int(input())
for i in range(n):
    plan = input()
    dq = deque(a) # 필수과목을 큐로
    for x in plan: # 현수의 과목을 하나씩 빼보면서
        if x in dq: # 필수과목에 현수의 과목이 들어가있으면?
            if x != dq.popleft(): # 그런데 필수과목의 첫번째와 현수의 과목이 같지 않으면? NO출력
                print('#%d NO' %(i+1))
                break # for문을 멈춰버림
    else: # 정상적으로 끝났을때 (순서 통과)
        if len(dq) == 0: # 필수과목이 안남았을때
            print('#%d YES' %(i+1))
        else: # 필수과목이 남았을때
            print('#%d NO' %(i+1))

