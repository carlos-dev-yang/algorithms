import sys
from collections import deque

sys.stdin = open('bfs_count_island.txt', 'r')
n=int(input())
island=[list(map(int, input().split())) for _ in range(n)]

end=(n-1, n-1)
cnt=0

dx=[0, 1, 1, 1, 0 , -1, -1, -1]
dy=[-1, -1, 0, 1, 1, 1, 0, -1]


def BFS(s, e):
  print('in bfs', s, e)
  que=deque([(s, e)])

  while que:
    row, col=que.popleft()

    if island[row][col] > 0:
      island[row][col]=0
      for k in range(8) :
        nr, nc = row+dx[k], col+dy[k]
        if 0 <= nr < n and 0 <= nc < n:
          que.append((nr, nc))
  for x in island:
    print(x)
  

for i in range(n):
  for j in range(n):
    if island[i][j]==1:
      cnt+=1
      BFS(i, j)

print(cnt)
