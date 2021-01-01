import sys
from collections import deque
#sys.stdin=open("input", "r")

n, m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
a=deque(a)
cnt = 0

while a: # a라는 자료구조가 비어있으면 멈춤
    if len(a) == 1: # 한명이 남았을 때, 그 사람도 보트타고 나감
        cnt += 1
        break
    if a[0]+a[-1] > m:
        a.pop() # 제일 무거운 한 사람 타고감 pop
        cnt += 1
    else: # 두사람이 같이 타고간 경우
        a.popleft() # 데크를 썼을 때 더욱 효과적인 popleft()함수
        a.pop()
        cnt += 1
print(cnt)

