import sys
#sys.stdin=open("input", "r")

def Count(len):
    cnt = 1 # 첫 말의 위치
    ep = Line[0] # 첫 마구간의 위치
    for i in range(1, n):
        if Line[i]-ep >= len: # 두 마구간 사이의 거리가 mid보다 크거나 같으면
            cnt += 1 # 말을 배치한다
            ep = Line[i] # 엔드포인트를 말이 배치된 위치로 재설정
    return cnt # 배치한 말의 마릿수를 리턴

n, c = map(int,input().split())
Line = []
for _ in range(n):
    tmp = int(input())
    Line.append(tmp)
Line.sort()

lt = 1
rt = Line[n-1] # 배열의 최대값
res = 0
while lt<=rt:
    mid = (lt+rt)//2 # 두 말의 가장 가까운 거리
    if Count(mid) >= c:
        res = mid
        lt = mid + 1 # 더 긴거리(좋은 답)을 찾아서감
    else:
        rt = mid - 1 # 길이가 너무 길어서 그 길이에 말이 전부 안들어감
print(res)
