import sys
sys.stdin = open('dfs_double_arm_scale.txt', 'r')
n=int(input())

v=list(map(int, input().split()))
res=[]

total=sum(v)

res=set()
cnt=0

lw=0
rw=0

def DFS(L, sum):
  global res
  if L==n:
    if 0<sum<=total:
      res.add(sum)
    return
  else:
    DFS(L+1, sum+v[L])
    DFS(L+1, sum-v[L])
    DFS(L+1, sum)
    
DFS(0, 0)
print(total-len(res))