import sys
sys.stdin = open('dfs_max_income_before_vacation.txt', 'r')
n=int(input())

pv=[]
pt=[]
res=-2147000000

for _ in range(n):
  t,v=(tuple(map(int, input().split())))
  pt.append(t)
  pv.append(v)

def DFS(L, time, value, remain):
  global res
  if L==n:
    if value>res:
      res=value
    return
  if remain==0:
    remain=pt[L]-1
    DFS(L+1, time+pt[L], value+pv[L], remain)
  else:
    remain-=1
    DFS(L+1, time, value, remain)
    
DFS(0, 0, 0, 0)
print(res)