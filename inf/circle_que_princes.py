import sys
from collections import deque
sys.stdin = open('circle_que_princes.txt', 'r')
n, k=map(int, input().split())
res=''
que=deque(range(1, n+1))

i=1
while que:
  if i==k:
    que.popleft()
    i=1
  else:
    que.append(que.popleft())
    i+=1
  
  if len(que)==1:
    res=que.pop()
    break

print(res)