import sys
sys.stdin = open('storage_platten.txt', 'r')
n=int(input())
a=list(map(int, input().split()))
m=int(input())

print(n, a, m)

for i in range(m):
  tp=-1
  lp=-1
  tmp_t=0
  tmp_l=2**31-1
  for j in range(n):
    if a[j]>tmp_t:
      tp=j
      tmp_t=a[j]
    if a[j]<tmp_l:
      lp=j
      tmp_l=a[j]
    
  a[tp]=a[tp]-1
  a[lp]=a[lp]+1


print(max(a)-min(a))


