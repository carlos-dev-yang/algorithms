import sys
sys.stdin = open('dfs_coin_changer.txt', 'r')
input=sys.stdin.readline
n=int(input())
coins=list(map(int, input().split()))
coins.sort(reverse=True)
total=int(input())
res=2147000000

def DFS(L, sum):
  global res
  if L>res:
    return
  if sum>total:
    return
  if sum==total:
    if res>L:
      res=L
  else:
    for i in coins:
      DFS(L+1, sum+i)

DFS(0, 0)
print(res)