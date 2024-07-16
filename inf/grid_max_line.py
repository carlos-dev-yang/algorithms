import sys
sys.stdin = open('grid_max_line.txt', 'r')
n=int(input())

grid=[list(map(int, input().split())) for _ in range(n)]

max=0
dig_r=0
dig_l=0

for i in range(n):
  row_tmp=col_tmp=0
  for j in range(n):
    row_tmp+=grid[i][j]
    col_tmp+=grid[j][i]
    if (i==j):
      dig_r+=grid[i][j]
      dig_l+=grid[-i-1][-j-1]

  if max < row_tmp:
    max=row_tmp
  
  if max > col_tmp:
    max=col_tmp

if max < dig_r:
  max=dig_r

if max > dig_l:
  max=dig_l

print(max)