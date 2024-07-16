import sys
sys.stdin = open('dfs_count_path.txt', 'r')
maze=[]

N=7
for i in range(N):
  maze.append(list(map(int, input().split())))


n=len(maze)
end=(n-1, n-1)
cnt=0

def DFS(row, col):
  global cnt
  if (row, col) == end:
    cnt+=1
    return
  
  if 0 <= row < n and 0 <= col < n and maze[row][col] == 0:
    maze[row][col]=1

    DFS(row+1, col)
    DFS(row-1, col)
    DFS(row, col+1)
    DFS(row, col-1)

    maze[row][col]=0

    
DFS(0, 0)
print(cnt)