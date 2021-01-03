import sys
#sys.stdin = open("input.txt", "r")

a = input()
b = input()

str1 = dict()
str2 = dict()

for x in a: # 알파벳 한개씩
    str1[x] = str1.get(x, 0)+1 # 키값(알파뱃) = 알파뱃 없으면 0, 있으면 밸류에 +1

for x in b:
    str2[x] = str2.get(x, 0)+1

for i in str1.keys(): # str1의 키값들만 뽑아서
    if i in str2.keys(): # str2의 키값들과 비교했을때
        if str1[i] != str2[i]: # 밸류값들이 같지 않다면 NO
            print('NO')
            break
    else: # 키값들이 같지 않을때 NO
        print('NO')
        break
else:
    print('YES')
