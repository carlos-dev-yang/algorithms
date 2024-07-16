import sys
sys.stdin = open('prime_number.txt', 'r')
n=int(input())
ch=[0]*(n+1)
cnt=0

for i in range(2, n+1):
  if ch[i]==0:
    cnt+=1
    for j in range(i, n+1, i):
      print(j)
      ch[j]=1
print(cnt)