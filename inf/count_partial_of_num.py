import sys
sys.stdin = open('count_partial_of_num.txt', 'r')

n, r=map(int, input().split())
a=list(map(int, input().split()))

print(n, r)
print(a)

count=0
for i in range(n):
  tmp=a[i]
  for j in range(i+1, n):
    if tmp==r:
      count+=1
      break

    b=tmp+a[j]
    if b==r:
      count+=1
      break
    elif b<r:
      tmp=b
    elif b>r:
      break

print(count)
