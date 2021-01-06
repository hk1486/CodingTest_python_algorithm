import sys
#sys.stdin = open("input.txt", "r")
def DFS(x):
    if x > 7:
        return
    else:
        #print(x, end='') # 전위순회
        DFS(x*2)
        #print(x, end='') # 중위순회
        DFS(x*2+1)
        print(x, end='') # 후위순회

DFS(1)