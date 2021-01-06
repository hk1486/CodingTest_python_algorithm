# 재귀함수와 스택
# n에 3이 입력되면 1~3까지 출력되는 코드
import sys
#sys.stdin = open("input.txt", "r")

def DFS(x):
    if x>0:
        DFS(x-1)
        print(x,end=' ')

if __name__=="__main__":
    n = int(input())
    DFS(n)