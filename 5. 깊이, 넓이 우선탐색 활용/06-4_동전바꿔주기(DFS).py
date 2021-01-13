import sys
sys.stdin = open("input.txt", "r")

def DFS(L, sum):
    global res
    if sum > t:
        return
    if L == k:
        if sum == t:
            res += 1
    else:
        for i in range(Q[L]+1): # 같은 레벨에서 동전의 개수만큼 for문이 돌아야함
            DFS(L+1, sum+(M[L]*i))

if __name__ == '__main__':
    t = int(input())
    k = int(input())
    M = []
    Q = []
    for i in range(k):
        a, b = map(int,input().split())
        M.append(a)
        Q.append(b)
    res = 0
    DFS(0,0)
    print(res)

