
import sys
#sys.stdin=open("input.txt","rt")

n = int(input())

for i in range(n):
    s = input()
    s = s.upper() # 전부 대문자로 바꿔줌
    if s == s[::-1]: # 파이썬스럽게 문자 거꾸로 바꿔주기
        print("#%d YES" %(i+1))
        
    else:
        print("#%d NO" %(i+1))

    """
    size = len(s)
    for j in range(size//2):
        if s[j] != s[-1-j]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))
    """
    