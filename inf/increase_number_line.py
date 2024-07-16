import sys
from collections import deque

sys.stdin = open('increase_number_line.txt', 'r')
n=int(input())
p=list(map(int, input().split()))

last=0
lt=0
rt=n-1
res=""
while lt<=rt:
  temp=[]

  if p[lt]>last:
    temp.append((p[lt], 'L'))
  if p[rt]>last:
    temp.append((p[rt], 'R'))
  temp.sort()

  if len(temp)==0:
    break
  else:
    res+=temp[0][1]
    last=temp[0][0]
    if temp[0][1]=='L':
      lt+=1
    else:
      rt-=1
  temp.clear()

print(res)