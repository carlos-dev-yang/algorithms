import sys
import heapq as hq
sys.stdin = open('dfs_binary_tree.txt', 'r')
n=list(map(int, input().split()))

def pre_order(arr, i, LR):
  print(i, LR)
  if i >= len(arr):
    return
  print('val', arr[i])

  pre_order(arr, 2*i+1, 'L')
  pre_order(arr, 2*i+2, 'R')

print('pre_order')
pre_order(n, 0, '')

def mid_order(arr, i, LR):
  print(i, LR)
  if i>=len(arr):
    return
  
  mid_order(arr, 2*i+1, 'L')
  print('val', arr[i])
  mid_order(arr, 2*i+2, 'R')

print('mid_order')
mid_order(n, 0, '')

def post_order(arr, i, LR):
  print(i, LR)
  if i>=len(arr):
    return
  
  post_order(arr, 2*i+1, 'L')
  post_order(arr, 2*i+2, 'R')
  print('val', arr[i])

print('post_order')
post_order(n, 0, '')