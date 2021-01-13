import sys
sys.stdin = open("input.txt", "r")

def DFS(L,total, time):
    global res
    if time > m:
        return
    elif L == n:
        if total > res:
            res = total
    else:
        DFS(L+1,total+score_lst[L],time+time_lst[L])
        DFS(L+1,total,time)

if __name__ == '__main__':
    n, m = map(int,input().split())
    score_lst = []
    time_lst = []
    for i in range(n):
        a, b = map(int,input().split())
        score_lst.append(a)
        time_lst.append(b)
    res = -2147000000
    DFS(0,0,0)
    print(res)