import sys
sys.stdin = open('dfs_change_coin.txt', 'r')
T=int(input())
K=int(input())

cv=list()
cn=list()
for _ in range(K):
  v, n=map(int, input().split())
  cv.append(v)
  cn.append(n)

cnt=0
res=[]

def DFS(L, sum):
  global cnt
  if sum>T:
    return
  if L==K:
    if sum==T:
      cnt+=1
    return
  else:
    for i in range(cn[L]+1):
      DFS(L+1, sum+(cv[L]*i))

    
DFS(0, 0)

print(cnt)