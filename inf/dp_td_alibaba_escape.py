import sys
sys.stdin = open('dp_td_alibaba_escape.txt', 'r')
n=int(input())
arr=[]
for _ in range(n):
  tmp=list(map(int, input().split()))
  arr.append(tmp)


dy=[[0]*(n) for x in range(n)]

def DFS(row, col):
  if dy[row][col]>0:
    return dy[row][col]
  if row == 0 and col == 0:
    return arr[0][0]
  
  if col==0:
    dy[row][col]=DFS(row-1, col)+arr[row][col]
  elif row==0:
    dy[row][col]=DFS(row, col-1)+arr[row][col]
  else:
    dy[row][col]=min(DFS(row-1, col), DFS(row, col-1))+arr[row][col]
  return dy[row][col]

DFS(n-1, n-1)
for x in dy:
  print(x)

print(dy[n-1][n-1])