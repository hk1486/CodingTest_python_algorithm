import sys
#sys.stdin=open("input", "r")

def Count(capacity):
    cnt = 1
    sum = 0
    for x in a:
        if sum+x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x
    return cnt

n, m = map(int,input().split())
a = list(map(int, input().split()))
maxx = max(a) # 가장 길이가 긴 노래
lt = 1
rt = sum(a)
res = 0

while lt<=rt:
    mid = (lt + rt)//2 # DVD 한장의 용량을 mid로
    if mid>=maxx and Count(mid) <= m:  # DVD 한장의 용량은 길이가 최대인 노래를 무조건 담을 정도의 용량이어야함
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1
print(res)
