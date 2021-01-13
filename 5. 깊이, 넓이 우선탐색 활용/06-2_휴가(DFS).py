import sys
sys.stdin = open("input.txt", "r")
def DFS(L, money):
    global res
    if L == n+1:
        if res < money:
            res = money
    else:
        if L+time_lst[L] <= n+1: # 가지를 뻗어나갈때 n+1일까지만 뻗어가면된다
            DFS(L+time_lst[L], money+money_lst[L]) # 레벨에 상담시간 더해주고, 금액 더해주고
        DFS(L+1,money) # 상담 안한다면 레벨에 날짜만 증가, 금액은 그대로

if __name__ == '__main__':
    n = int(input())
    time_lst = []
    money_lst = []
    for i in range(n):
        a, b = map(int,input().split())
        time_lst.append(a)
        money_lst.append(b)
    res = -2147000000
    time_lst.insert(0,0) # 배열의 인덱스를 레벨로 보기 위해서 한칸씩 밀어줌
    money_lst.insert(0,0)
    DFS(1,0)
    print(res)