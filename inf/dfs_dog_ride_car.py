import sys
sys.stdin = open('dfs_dog_ride_car.txt', 'r')
limit, n=map(int, input().split())
arr=list(int(input()) for _ in range(n))
max=0
def DFS(L, sum, tsum):
  global max
  if sum+(limit-tsum)<max:
    return
  if sum>limit:
    return
  if L==n:
    if sum>max:
      max=sum
  else:
    DFS(L+1, sum+arr[L], tsum+arr[L])
    DFS(L+1, sum, tsum+arr[L])

DFS(0, 0, 0)
print(max)