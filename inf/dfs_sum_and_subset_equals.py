import sys
import heapq as hq
sys.stdin = open('dfs_sum_and_subset_equals.txt', 'r')
n=int(input())
arr=list(map(int, input().split()))
tot=sum(arr)

def pre_order(i, subset):
  if subset > tot//2:
    return
  if i==n:
    if subset==(tot-subset):
      print('YES')
      sys.exit(0)
  else:
    pre_order(i+1, subset+arr[i])
    pre_order(i+1, subset)

pre_order(0, 0)
print('NO')