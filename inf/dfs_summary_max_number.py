import sys
sys.stdin = open('dfs_summary_max_number.txt', 'r')
n, m=map(int, input().split())

pv=[]
pt=[]
res=-2147000000

for _ in range(n):
  v, t=(tuple(map(int, input().split())))
  pv.append(v)
  pt.append(t)

def DFS(L, time, value):
  global res
  if time>m:
    return
  if L==n:
    if value>res:
      res=value
    return
  DFS(L+1, time+pt[L], value+pv[L])
  DFS(L+1, time, value)
    
DFS(0, 0, 0)
print(res)