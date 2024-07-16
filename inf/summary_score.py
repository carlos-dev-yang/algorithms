import sys
sys.stdin = open('summary_score.txt', 'r')
n=int(input())

tmp=list(map(int, input().split()))

sum=0
cnt=0

for x in tmp:
  if x==1:
    cnt+=1
    sum+=cnt
  else:
    cnt=0

print(sum)
