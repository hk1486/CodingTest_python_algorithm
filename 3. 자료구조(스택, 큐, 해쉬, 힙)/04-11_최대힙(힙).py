import sys
#sys.stdin = open("input.txt", "r")
import heapq

a = []
while True: # 입력 받기 위해
   n = int(input())
   if n == -1: # 프로그램 종료
       break
   if n == 0: # 0일때 pop
       if len(a) == 0: # 힙에 아무것도 없을 수도 있기 때문에
           print(-1) # 출력할 자료가 없으면 -1
       else:
           print(-heapq.heappop(a)) # 루트노드값 pop하면서 음수화
   else:
       heapq.heappush(a, -n) # a리스트에 n값을 음수로 push
