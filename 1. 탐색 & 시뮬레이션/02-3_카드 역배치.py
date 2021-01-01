
import sys
# sys.stdin=open("input.txt","rt")

a = list(range(21)) # 1~20까지 있는 리스트 만들기

for _ in range(10): # '_'가 들어가면 변수없이 그냥 반복
    s, e = map(int,input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i]
a.pop(0) # a배열의 0번째를 빼준다.
for x in a:
    print(x,end=' ')

