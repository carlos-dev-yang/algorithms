import sys
from collections import deque
sys.stdin = open('emergency_patient.txt', 'r')
n, k=map(int, input().split())

Q=deque([(pos, val) for pos, val in enumerate(list(map(int, input().split())))])

cnt=0
while Q:
  cur=Q.popleft()

  if any(cur[1]<x[1] for x in Q):
    Q.append(cur)
  else:
    cnt+=1
    if cur[0]==k:
      print(cnt)
      break