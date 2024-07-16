import sys
sys.stdin = open('dp_floyd_chair_person.txt', 'r')
n=int(input())
# n,m=map(int, input().split())
fri=[[n]*(n+1) for _ in range(n+1)]

for i in range(1, n+1):
  fri[i][i]=0

while True:
  a,b=map(int, input().split())
  if a==-1:
    break
  fri[a][b]=1
  fri[b][a]=1

for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      fri[i][j]=min(fri[i][j], fri[i][k]+fri[k][j])

score=5
res=[]
for i in range(1, n+1) :
  max_p=max(fri[i][1:])
  score=min(score, max_p)
  res.append(max_p)

print(score, end=' ')
print(res.count(score), end=' ')
print()
for i in range(n):
  if score==res[i]:
    print(i+1, end=' ')