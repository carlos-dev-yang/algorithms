import sys
sys.stdin = open('dfs_guess_line_number.txt', 'r')
n, f=map(int, input().split())
p=[0]*n
b=[1]*n
ch=[0]*(n+1)

for i in range(1, n):
  b[i]=b[i-1]*(n-i)//i

def DFS(L):
  
  if L==n:
    sum=0
    for i in range(n):
      sum+=p[i]*b[i]
    if sum==f:
      for x in p:
        print(x, end=' ')
      sys.exit()
    return
  else:
    for i in range(1, n+1):
      if ch[i]==0:
        ch[i]=1
        p[L]=i
        DFS(L+1)
        ch[i]=0

DFS(0)