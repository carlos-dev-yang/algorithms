import sys
from collections import deque

sys.stdin = open('dfs_bfs_home_numbering.txt', 'r')
n=int(input())
town=[]
for i in range(n):
  town.append(list(map(int, input()))) 

end=(n-1, n-1)
ch=[[0]*n for _ in range(n)]
cnt=0
res=[]

def DFS(row, col):
  global cnt
  if town[row][col] == 0:
    return

  if ch[row][col] > 0:
    return
  
  ch[row][col]=cnt

  for nr, nc in ((row+1, col), (row-1, col), (row, col+1), (row, col-1)):
    if 0 <= nr < n and 0 <= nc < n and ch[nr][nc] == 0:
      DFS(nr, nc)

def BFS():
  global cnt
  que=deque([(0, 0)])
  visited=set([0, 0])

  while que:
    row, col=que.popleft()
    visited.add((row, col))

    if (row,col) == (n-1, n-1):
      break

    if town[row][col] > 0 and ch[row][col] == 0:
      cnt+=1
      DFS(row, col)

    for nr, nc in ((row+1, col), (row-1, col), (row, col+1), (row, col-1)):
      if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
        que.append((nr, nc))


BFS()

for x in ch:
  print(x)
print(cnt)