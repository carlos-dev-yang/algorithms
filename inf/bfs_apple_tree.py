import sys
from collections import deque
sys.stdin = open('bfs_apple_tree.txt', 'r')
n=int(input())
farm=[]

for i in range(n):
  farm.append(list(map(int, input().split())))

def harvest_apple_diamond(FARM):
  N = len(FARM)
  center=N//2
  visited=set()
  que=deque([(center, center, 0)])
  sum=0
  max_dist=N//2

  while que:
    row, col, dist = que.popleft()

    if dist > max_dist:
      print(visited)
      print(sum)
      return
    
    if (row, col) not in visited:
      visited.add((row, col))
      sum+=FARM[row][col]

      for new_row, new_col in ((row+1, col), (row-1, col), (row, col+1),(row, col-1)):
        if 0 <= new_row < n and 0 <= new_col < n:
          que.append((new_row, new_col, dist+1))


harvest_apple_diamond(farm)