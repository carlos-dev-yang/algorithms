import sys
from collections import deque

sys.stdin = open('bfs_tomato_storage.txt', 'r')
m,n=map(int,input().split())

storage=[list(map(int, input().split())) for _ in range(n)]
res=0

dx=[0, 1, 0, -1]
dy=[-1, 0, 1, 0]

days=0
que=deque()

for i in range(n):
  for j in range(m):
    if storage[i][j]>0:
      que.append((i, j, 1))

while que:
  row, col, day=que.popleft()

  storage[row][col] = day
  if days < day:
    days=day

  for k in range(4) :
    nr, nc = row+dx[k], col+dy[k]
    if 0 <= nr < n and 0 <= nc < m:
      if storage[nr][nc] == 0:
        que.append((nr, nc, day+1))

not_ripen=0
for i in range(n):
  for j in range(m):
    if storage[i][j] == 0:
      not_ripen+=1

if not_ripen > 0:
  print(-1)
else:
  print(days-1)