import sys
#sys.stdin = open("input.txt", "r")

def DFS(L,total):
    global res
    if L == n:
        if 0 < total < sum+1:
            res.add(total) # set에 더해줄땐 add함수
    else:
        DFS(L+1, total+water[L]) # 가장 왼쪽 노드엔 더해주기
        DFS(L+1, total-water[L]) # 가운데 노드는 빼주기
        DFS(L+1, total)          # 가장 오른쪽 노드는 값 그대로

if __name__ == '__main__':
    n = int(input())
    water = list(map(int,input().split()))
    res = set() # 중복을 방지하기 위해 set()
    sum = sum(water)
    DFS(0,0)
    print(sum - len(res))
