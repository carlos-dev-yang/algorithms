import sys
sys.stdin = open('dfs_count_path_hiking.txt', 'r')
n=int(input())
mt=[]
for i in range(n):
  mt.append(list(map(int, input().split())))


end=(n-1, n-1)
cnt=0
ch=[[0]*n for _ in range(n)]

def DFS(row, col):
  global cnt
  if (row, col) == end:
    cnt+=1
    return
  
  for nx, ny in ((row+1, col), (row-1, col), (row, col+1), (row, col-1)):
    if 0 <= nx < n and 0 <= ny < n and ch[nx][ny] == 0 and mt[nx][ny] > mt[row][col]:
      ch[nx][ny]=1
      DFS(nx, ny)
      ch[nx][ny]=0

    
DFS(0, 0)
print(cnt)