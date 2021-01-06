import sys
#sys.stdin = open("input.txt", "r")

def DFS(x):
    if x == 0: # 주어진 인자가 0이 되면 종료
        return
    else:
        DFS(x//2)
        print(x % 2, end='')

n = int(input())
DFS(n)
