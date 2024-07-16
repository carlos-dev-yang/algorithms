import sys
sys.stdin = open('dp_floyd_city_path.txt', 'r')
n,m=map(int, input().split())
dis=[[5000]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
  dis[i][i]=0

for i in range(m):
  a,b,c=map(int, input().split())
  dis[a][b]=c

for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      if i==1 and j==5:
        print(dis[i])
        print(i, j, k, min(dis[i][j], dis[i][k]+dis[k][j]))
      dis[i][j]=min(dis[i][j], dis[i][k]+dis[k][j])
  print()

for x in dis:
  for y in x:
    if y==5000:
      print('M', end=' ')
    else:
      print(y, end=' ')
  print()
