import sys
sys.stdin = open('dp_raise_tower.txt', 'r')
n=int(input())
arr=[]
for _ in range(n):
  arr.append(list(map(int, input().split())))

arr.sort(reverse=True)

dy=[0]*(n+1)
dy[0]=arr[0][1]
res=0
for i in range(1, n):
  max_h=0
  for j in range(i-1, -1, -1):
    if arr[j][2] > arr[i][2] and dy[j] > max_h:
      max_h=dy[j]
  dy[i]=max_h+arr[i][1]
  res=max(res, dy[i])

print(res)
      