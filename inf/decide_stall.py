import sys
sys.stdin = open('decide_stall.txt', 'r')
n, m=map(int, input().split())

def Count(len):
  cnt=1
  ep=Line[0]
  for i in range(1, n):
    if Line[i]-ep>=len:
      cnt+=1
      ep=Line[i]

  return cnt

Line=[]
longest=0
for i in range(n):
  s=int(input())
  Line.append(s)

Line.sort()

lt=0
rt=Line[n-1]

cnt=1
res=0
while lt<=rt:
  mid=(lt+rt)//2
  if Count(mid)>=m:
    res=mid
    lt=mid+1
  else:
    rt=mid-1

print(res)