import sys
from collections import deque
sys.stdin = open('graph_topological_sort.txt', 'r')
# n=int(input())
n,m=map(int, input().split())
graph=[[0]*(n+1) for _ in range(n+1)]

# degree=[0]*(n+1)
degree=[0]*n
q=deque([])
res=[]
degree.insert(0, -1)

for i in range(1, n+1):
  a,b=map(int, input().split())
  graph[a][b]=1
  degree[b]+=1

for i in range(1, n+1):
  if degree[i]==0:
    degree[i]=-1
    q.append(i)

while q:
  cur=q.popleft()
  print(cur, end=' ')
  
  for i in range(1, n+1):
    if graph[cur][i]==1:
      degree[i]-=1
      if degree[i]==0:
        q.append(i)
