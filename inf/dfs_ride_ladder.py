import sys
from collections import deque

sys.stdin = open('dfs_ride_ladder.txt', 'r')
ladder=[list(map(int, input().split())) for _ in range(10)]
ch=[[0]*10 for _ in range(10)]
n=len(ladder)
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

end=2

def DFS(row, col, start):
  if ladder[row][col]==0:
    return
  
  if row==n-1:
    if ladder[row][col]==end:
      print(start)
    return

  for k in range(4):
    nr, nc = row+dy[k], col+dx[k]
    if 0 <= nr < n and 0 <= nc < n and ladder[nr][nc]>0 and ch[nr][nc]==0:
      ch[nr][nc]=1
      DFS(nr, nc, start)
      ch[nr][nc]=0
      break

for i in range(n):
  DFS(0, i, i)