import sys
#sys.stdin=open("input", "r")

n = int(input())
body = []
for _ in range(n):
    h, w = map(int,input().split())
    body.append((h,w))
cnt = 0
largest = 0
body.sort(reverse=True)

for x, y in body:
    if y > largest:
        largest = y
        cnt += 1
print(cnt)


