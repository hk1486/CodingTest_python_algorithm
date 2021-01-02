import sys
#sys.stdin=open("input", "r")

stack = []
a = input()

for x in a: # 후위표기식에서
    if x.isdecimal(): # 숫자인 경우
        stack.append(int(x)) # x를 정수화시켜 넣어줌
    else:
        if x == '+':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 + n1)
        elif x == '-':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 - n1)
        elif x == '*':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2 * n1)
        elif x == '/':
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append(n2/n1)
print(stack[0]) # 결국 남은건 스택의 0번 자료

