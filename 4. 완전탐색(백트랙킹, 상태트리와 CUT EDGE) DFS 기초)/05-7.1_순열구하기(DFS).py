import sys
#sys.stdin = open("input.txt", "r")

def DFS(L):
    global cnt
    if L == m: # 레벨이 m(뽑는 개수)이 될 때
        for j in range(L): # 레벨만큼 돌면서 찾음
            print(res[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1): # 순열 1부터 n까지 돌면서
          if ch[i] == 0: # i번째 체크리스트가 0일 때
            ch[i] = 1 # 1로 체크
            res[L] = i # 해당 레벨의 결과값을 i로 바꿔줌
            DFS(L+1) # 레벨 하나 증가
            ch[i] = 0 # 0으로 체크

if __name__ == '__main__':
    n, m = map(int,input().split())
    res = [0] * n # 결과값
    ch = [0] * (n+1) # 중복x 위한 체크리스트
    cnt = 0
    DFS(0)
    print(cnt)
