import sys
sys.stdin = open('reversed_sequence.txt', 'r')
n=int(input())
a=list(map(int, input().split()))

ab=[0]*n

for i in range(n):
  tmp=a[i]
  # print(tmp)

  p=0
  j=0
  while j<n:
    if ab[j]==0:
      if p==tmp:
        break
      p+=1
    j+=1
  ab[j]=i+1

print(ab)
