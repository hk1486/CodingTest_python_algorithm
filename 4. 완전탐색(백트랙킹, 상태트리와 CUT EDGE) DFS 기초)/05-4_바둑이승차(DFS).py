import sys
#sys.stdin = open("input.txt", "r")

def DFS(L, sum):
    global result
    if c > W:
        result = W
        return
    if sum > c:
        return
    if L == n:
        if sum > result:
            result = sum
    else:
        DFS(L+1, sum+w[L])
        DFS(L+1, sum)

if __name__ == "__main__":
    c, n = map(int,input().split())
    w = [0]*n
    for i in range(n):
        w[i] = int(input())
    result = -2147000000
    W = sum(w)
    DFS(0, 0)
    print(result)
