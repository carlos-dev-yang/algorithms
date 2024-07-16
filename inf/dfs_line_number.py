import sys
sys.stdin = open('dfs_line_number.txt', 'r')
input=sys.stdin.readline
n, m=map(int, input().split())

ch=[0]*(n+1)
res=[0]*n
cnt=0
def DFS(L):
  global cnt
  if L==m:
    for j in range(L):
      print(res[j], end=' ')
    print()
    cnt+=1
  else:
    for i in range(1, n+1):
      if ch[i]==0:
        ch[i]=1
        res[L]=i
        DFS(L+1)
        ch[i]=0

DFS(0)