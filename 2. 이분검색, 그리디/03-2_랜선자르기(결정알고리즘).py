import sys
#sys.stdin=open("input", "r")

def Count(len): # 이분검색을 위한 함수
    cnt = 0
    for x in Line:
        cnt += (x//len)
    return cnt

k, n = map(int,input().split())
Line = []
res = 0
largest = 0
for i in range(k):
    tmp = int(input())
    Line.append(tmp)
    largest = max(largest, tmp) # 가장 긴 랜선

lt = 1
rt = largest
while lt<=rt: # 이분검색
    mid = (lt + rt)//2
    if Count(mid) >= n: # 랜선의 길이가 나누고자 하는 개수보다 크거나 같으면
        res = mid
        lt = mid+1 # 더 좋은 답을 찾아서감
    else: # 답이 되지 않을 때
        rt = mid-1
print(res)




