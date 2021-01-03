import sys
#sys.stdin = open("input", "r")

# 딕셔너리로 해결하면 쉬운 문제
n = int(input())
p = dict()
for i in range(n): # n개의 단어를 dict에 저장
    word = input()
    p[word] = 1 # 단어의 개수는 한개씩

for i in range(n-1):
    word = input()
    p[word] = 0 # 쓰인 단어들만 값을 0으로 바꿔줌

for key, value in p.items():
    if value == 1: # 아직 값이 바뀌지 않은 키값만 뽑아줌
        print(key)
        break