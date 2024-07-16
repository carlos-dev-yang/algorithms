import sys
from collections import deque
sys.stdin = open('bfs_path_finding.txt', 'r')
MAZE=[]

for i in range(7):
  MAZE.append(list(map(int, input().split())))

def path_finding(maze):
  n = len(maze)
  visited=set()
  que=deque([(0, 0, 0)])
  end=(n-1, n-1)

  while que:
    row, col, dist = que.popleft()

    if (row, col) == end :
      print(dist)
      return
    
    if (row, col) not in visited and maze[row][col] != 1:
      visited.add((row, col))

      for new_row, new_col in ((row+1, col), (row-1, col), (row, col+1),(row, col-1)):
        if 0 <= new_row < n and 0 <= new_col < n:
          que.append((new_row, new_col, dist+1))
  else:
    print(-1)

path_finding(MAZE)