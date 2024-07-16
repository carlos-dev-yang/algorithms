import sys
sys.stdin = open('gotgam_sand_glass.txt', 'r')
n=int(input())
grid=[list(map(int, input().split())) for _ in range(n)]

m=int(input())
rot=[list(map(int, input().split())) for _ in range(m)]

res=0
s=0
e=n

for i in range(m):
  r,d,c=rot[i]
  for j in range(c):
    if d==0:
      grid[r-1].append(grid[r-1].pop(0))
    else:
      grid[r-1].insert(0, grid[r-1].pop())

for x in grid:
  print(x)

for i in range(n):
  for j in range(s, e):
    res+=grid[i][j]

  if i<n//2:
    s+=1
    e-=1
  else:
    s-=1
    e+=1

print(res)

 