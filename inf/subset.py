import sys
import heapq as hq
sys.stdin = open('subset.txt', 'r')
n=int(input())
ch=[0]*(n+1)

def pre_order(i, subset, LR):
  if i > n:
    for j in range(len(subset)):
      if subset[j]==1:
        print(j, end=' ')
    print()
    return

  subset[i]=1
  pre_order(i+1, subset, 'L')
  subset[i]=0
  pre_order(i+1, subset, 'R')

pre_order(1, ch, '')