import sys
from collections import deque

sys.stdin = open('titanic_escape.txt', 'r')
n, m=map(int, input().split())
p=list(map(int, input().split()))
res=0
p.sort()

p=deque(p)
while p:
  ln=len(p)
  if ln==1:
    p.pop()
  elif p[0]+p[ln-1]>m:
    p.pop()
  else:
    p.popleft()
    p.pop()
  res+=1
print(res)