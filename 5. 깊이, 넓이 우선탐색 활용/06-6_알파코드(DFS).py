import sys
sys.stdin = open("input.txt", "r")

def DFS(L,P):
    global cnt
    if L == n:
        cnt += 1
        for j in range(P): # 알파벳으로 출력하기 위함, 인덱스 0부터 P까지
            print(chr(res[j]+64),end='') # chr로 변환해주고 아스키코드 A:65 니까 64를 더해줌
        print()

    else:
        for i in range(1,27): # 알파벳 26개의 가닥을 뻗음
            if code[L]==i:    # 코드의 L번째 인덱스 값이 i일때
                res[P]=i      # res배열에 i를 넣어줌
                DFS(L+1,P+1)  # 레벨도 더해주고, 인덱스도 더해줌
            # 두자리의 숫자(예:25)가 들어왔을때,
            # code[L]의값이 i의 10의자리숫자(2)와 1의자리숫자(5)가 같으면
            elif i >= 10 and code[L] == i//10 and code[L+1] == i%10:
                res[P]=i      # res배열에 두자리숫자 더해줌
                DFS(L+2,P+1)  # 두자리 숫자니까 레벨 2 더해주고, 인덱스도 더해줌

if __name__ == "__main__":
    code = list(map(int,input()))
    n=len(code) # 종착점
    code.insert(n,-1) # i가 26까지 돌기때문에, 맨 마지막 숫자가 1 또는 2이면
                      # 19라인에 걸려서 그 뒤 숫자까지 확인해야하는 인덱스에러가 날 수 있음
                      # 그것을 방지하기 위해 무조건 False로 걸리는 -1을 맨뒤에 넣어줌

    res = [0]*(n+3) # 공간을 넉넉히 잡기위해
    cnt = 0
    DFS(0,0)
    print(cnt) # 글자개수