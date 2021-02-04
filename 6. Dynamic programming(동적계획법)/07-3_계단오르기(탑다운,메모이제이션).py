import sys
sys.stdin = open("input.txt",'r')

def DFS(len):
    if dy[len] > 0: # 메모이제이션 : 값이 있으면 그냥 리턴해버리면됨
        return dy[len]
    if len == 1 or len == 2: # 1과 2는 미리 구해놓음
        return len
    else:
        dy[len] = DFS(len-1) + DFS(len-2)
        return dy[len]

if __name__ == "__main__":
    n = int(input())
    dy = [0]*(n+1)
    print(DFS(n))