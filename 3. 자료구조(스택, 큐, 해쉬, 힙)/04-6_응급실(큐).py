import sys
#sys.stdin=open("input", "r")
from collections import deque

n, m = map(int,input().split())
a = [ (pos, value) for pos, value in enumerate(list(map(int,input().split())))]
# 인덱스값과 리스트의 값을 같이 받아줌

a = deque(a)
cnt = 0
while True:
    b = a.popleft()
    # any함수를 사용해 환자의 위험도가 단한명의 다른 환자의 위험도보다 낮을때
    if any(b[1] < x[1] for x in a):
        a.append(b) # 뒤로 보냄
    else:
        cnt += 1 # 만약 위험도가 제일 높으면 cnt + 1
        if b[0] == m: # 환자의 순서가 m 과 같으면 반복문 빠져나오기
            break
print(cnt)

