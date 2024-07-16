import sys
sys.stdin = open('dp_alibaba_escape.txt', 'r')
n=int(input())
arr=[]
for _ in range(n):
  tmp=list(map(int, input().split()))
  arr.append(tmp)


dy=[[0]*(n) for x in range(n)]
for i in range(n):
  dy[0][i]=dy[0][i-1]+arr[0][i]
  dy[i][0]=dy[i-1][0]+arr[i][0]

for i in range(1, n):
  for j in range(1, n):
    dy[i][j]=min(dy[i-1][j], dy[i][j-1])+arr[i][j]

for x in dy:
  print(x)

print(dy[n-1][n-1])