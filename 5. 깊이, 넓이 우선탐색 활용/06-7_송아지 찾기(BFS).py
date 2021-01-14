import sys
sys.stdin = open("input.txt", "r")
from collections import deque

MAX = 10000 # 좌표 맥시멈
ch = [0] * (MAX+1) # 체크리스트 크기 지정
dis = [0] * (MAX+1) # 거리좌표 크기 지정
n,m = map(int,input().split()) # 출발점과 도착점
ch[n] = 1 # 현재 내위치 체크
dis[n] = 0 # 현재 내위치 0레벨 부터 시작
dQ = deque()
dQ.append(n) # 데크에 출발점 추가
while dQ: # 데크가 비어있으면 멈춤
    now = dQ.popleft() # 현재위치 pop
    if now == m: # 현재위치가 도착지이면
        break
    for next in(now-1, now+1, now+5): # 내가 갈 수 있는 3가지 위치로 한번씩 이동 가능
        if 0<next<=MAX: #다음위치의 범위지정 음수x, 최대값 넘어갈 수 없음
            if ch[next] == 0: # 체크리스트에서 0인것만
                dQ.append(next) # 데크에 추가
                ch[next]=1 # 추가했으니 체크리스트 1로 체크
                dis[next] = dis[now]+1 # 거리좌표에서 다음 위치 레벨 1 증가
print(dis[m]) # 거리좌표에서 도착지의 값을 출력