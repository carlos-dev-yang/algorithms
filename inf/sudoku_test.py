import sys
sys.stdin = open('sudoku_test.txt', 'r')
n=9
a=[list(map(int, input().split())) for _ in range(n)]

res='YES'
for i in range(n):
  tx=[0]*n
  ty=[0]*n
  for j in range(n):
    if tx[a[i][j]-1]!=0 or ty[a[j][i]-1]!=0:
      res='NO'
      break
    tx[a[i][j]-1]=a[i][j]
    ty[a[j][i]-1]=a[j][i]
  if res=='NO':
    break
print(res)