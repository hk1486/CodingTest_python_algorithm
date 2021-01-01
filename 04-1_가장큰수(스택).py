import sys
#sys.stdin=open("input", "r")

num, m = map(int, input().split())
num = list(map(int, str(num)))

stack = []
for x in num:
    while stack and m > 0 and stack[-1]<x: # 리스트가 비어있지 않고, m이 0 보다 크고, 앞데이터가 현재 데이터보다 작을때
        stack.pop()
        m -= 1
    stack.append(x) # 그렇지 않은경우 스택에 쌓아줌
if m!=0:
    stack = stack[:-m] # 다 쌓았는데도 m이 아직 0이 아닌경우 뒤에서 -m만큼 잘라줌
for x in stack:
    print(x, end='')