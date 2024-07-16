import sys
from collections import deque
sys.stdin = open('theory_plan.txt', 'r')
prioty=input()
n=int(input())

for _ in range(n):
  PQ=deque(prioty)
  PG=list(input())
  for i in PG:
    if i in PQ:
      cur=PQ.popleft()
      if i!=cur:
        print('NO')
        break
  else:
    print('YES')
  