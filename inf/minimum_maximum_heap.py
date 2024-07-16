import sys
import heapq as hq
sys.stdin = open('minimum_maximum_heap.txt', 'r')

mn=[]
mx=[]

while True:
  s=int(input())

  if s==-1:
    break
  elif s==0:
    if mn:
      print(hq.heappop(mn))
      print(-hq.heappop(mx))
    else:
      print(-1)
  else:
    hq.heappush(mn, s)
    hq.heappush(mx, -s)

