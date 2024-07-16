import sys
sys.stdin = open('dfs_case_of_numbers.txt', 'r')
n, f=map(int, input().split())
p=list(map(int, input().split()))
t=int(input())

ch=[0]*(n+1)
cnt=0

def DFS(L, s, sum):
  global cnt
  if L==f:
    if sum%t==0:
      cnt+=1
  else:
    for i in range(s, n):
      DFS(L+1, i+1, sum+p[i])

DFS(0, 0, 0)
print(cnt)