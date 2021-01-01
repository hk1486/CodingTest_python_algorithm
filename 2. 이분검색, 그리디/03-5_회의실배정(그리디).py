import sys
#sys.stdin=open("input", "r")

n = int(input())
meeting = []
for i in range(n):
    s, e = map(int,input().split())
    meeting.append((s,e))
meeting.sort(key = lambda x : (x[1],x[0])) # 람다식을 써서 x의 인덱스 1번이 정렬 우선순위가 되어라
et = 0
cnt = 0
for s, e in meeting:
    if s >= et: # 처음 엔드타임은 0이고, 시작 시간이 엔드타임보다 크다면
        et = e # 엔드타임을 회의 끝나는 시간으로 설정
        cnt += 1 # 시작시간이 끝나는시간보다 같거나 크다면 회의수 +1
print(cnt)


