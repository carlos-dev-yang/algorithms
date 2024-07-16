import sys
sys.stdin = open('lan_cable_cut.txt', 'r')
n, m=map(int, input().split())

line=[]
res=0
largest=0

for i in range(n):
  tmp=int(input())
  line.append(tmp)
  largest=max(largest, tmp)


lt=1
rt=largest
res=0
while lt<=rt:
  mid=(lt+rt)//2
  count=0
  for i in range(n):
    count+=line[i]//mid

  if count>=m:
    res=mid
    lt=mid+1
  else:
    rt=mid-1

print(res)