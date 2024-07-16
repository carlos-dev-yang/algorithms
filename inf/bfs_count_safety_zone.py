import sys
from collections import deque

sys.stdin = open('bfs_count_safety_zone.txt', 'r')
n=int(input())
mt=[list(map(int, input().split())) for _ in range(n)]
res=0

dx=[0, 1, 0, -1]
dy=[-1, 0, 1, 0]


def BFS(N):
  global res
  cnt=0
  ch=[[0]*n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      if mt[i][j]>N and ch[i][j]==0:
        cnt+=1
        que=deque([(i, j)])

        while que:
          row, col=que.popleft()

          if mt[row][col] > N and ch[row][col]==0:
            ch[row][col]=1
            for k in range(4) :
              nr, nc = row+dx[k], col+dy[k]
              if 0 <= nr < n and 0 <= nc < n:
                que.append((nr, nc))
  if res < cnt:
    res=cnt

for l in range(1, 8):
  BFS(l)

print(res)
