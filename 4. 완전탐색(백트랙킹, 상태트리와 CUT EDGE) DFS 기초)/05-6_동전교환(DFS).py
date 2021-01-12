import sys
#sys.stdin = open("input.txt", "r")

def DFS(L,sum):
    global res
    if L > res:
        return
    if sum > m:
        return
    if sum == m:
        if L < res:
            res = L
    else:
        for i in range(n):
            DFS(L+1,sum+a[i])

if __name__ == '__main__':
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    res = 2147000000
    a.sort(reverse=True) # 1원부터 시작하면 너무 깊이내려감, 큰값부터 시작하자
    DFS(0,0)
    print(res)

