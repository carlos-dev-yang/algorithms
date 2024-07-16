import sys
sys.stdin = open('music_video.txt', 'r')
n, m=map(int, input().split())
a=list(map(int, input().split()))

print(a)

lt=0
rt=sum(a)
res=0
while lt<=rt:
  mid=(lt+rt)//2

  cnt=1
  tmp=0
  for i in range(n):
    if tmp+a[i] > mid:
      cnt+=1
      tmp=a[i]
    elif tmp+a[i] <= mid:
      tmp+=a[i]
  
  if cnt<=m:
    res=mid
    rt=mid-1
  else:
    lt=mid+1

print(res)