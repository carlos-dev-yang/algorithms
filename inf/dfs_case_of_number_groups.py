import sys
sys.stdin = open('dfs_case_of_number_groups.txt', 'r')
n, m=map(int, input().split())

cnt=0
res=[0]*(n+1)
def DFS(L, s):
  global cnt
  if L==m:
    for j in range(L):
      print(res[j], end=' ')
    cnt+=1
    print()
  else:
    for i in range(s, n+1):
      res[L]=i
      DFS(L+1, i+1)

DFS(0, 1)
print(cnt)