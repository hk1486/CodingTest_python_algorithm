
import sys
#sys.stdin=open("input.txt","rt")
a = input()
res = 0
for x in a:
    if x.isdecimal(): # 숫자인지 확인하는 함수
        res = res*10+int(x) # 숫자만 걸러서 res에 저장
print(res)
cnt = 0
for i in range(1,res+1):
    if res%i == 0:
        cnt += 1
print(cnt)