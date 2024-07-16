import sys
sys.stdin = open('dfs_dispense_coin.txt', 'r')
n=int(input())

cl=[]
M=[0]*3
T=0
res=2147000000

for _ in range(n):
  c=int(input())
  cl.append(c)
  T+=c

cnt=0

def DFS(L):
  global res
  global cnt
  
  if max(M)-(T-max(M))>res:
    return
  if L==n:
    diff=max(M)-min(M)
    if diff<res:
      tmp=set()
      for x in M:
        tmp.add(x)
      if len(tmp)==3:
        res=diff
    return
  else:
    cnt+=1
    for i in range(3):
      M[i]+=cl[L]
      DFS(L+1)
      M[i]-=cl[L]
    
DFS(0)

print(res)