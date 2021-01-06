import sys
#sys.stdin = open("input.txt", "r")

def DFS(v):
    if v == n+1: # DFS(4)가 될 때 출력
        for i in range(1,n+1):
            if ch[i] == 1: # 1~3까지 체크박스에 1로 체크된것들만 출력
                print(i,end = ' ')
        print() # 한줄 띄워줌
    else:
        ch[v] = 1 # 체크박스 바꿔주고 (해당숫자 들어간다 or 안들어간다)
        DFS(v+1) # DFS(4)가 될 때 까지 증가하며 탐색, 4가 되면 출력
        ch[v] = 0
        DFS(v+1)

n = int(input())
ch = [0] * (n+1) # 체크박스 선언
DFS(1) # DFS(1)부터 들어가면서 깊이우선탐색