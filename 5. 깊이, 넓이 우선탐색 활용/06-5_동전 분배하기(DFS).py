import sys
sys.stdin = open("input.txt", "r")

def DFS(L):
    global res
    if L == n:
        cha = max(money) - min(money)
        if cha < res:
            tmp = set()
            for x in money:
                tmp.add(x)
            if len(tmp)==3: # 세 사람의 총액은 다 달라야 하기에 중복장지를 위해 set을 써줌
                res=cha
    else:
        for i in range(3): # 3사람의 경우의 수
            money[i] += a[L] # i번째 사람한테 동전을 더해주고
             DFS(L+1) # 노드의 레벨 증가 다음 동전으로 감
            money[i] -= a[L] # 노드가 백할 때 합에서 해당 동전값을 빼줘야함

if __name__ == "__main__":
    n = int(input())
    a = []
    money = [0] * 3  # 각 사람의 동전 합을 저장할 리스트
    for _ in range(n):
        a.append(int(input()))
    res = 2147000000
    DFS(0)
    print(res)