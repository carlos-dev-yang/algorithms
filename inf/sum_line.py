import sys
sys.stdin = open('sum_line.txt', 'r')
n=int(input())
a=list(map(int, input().split()))

def digit_sum(x):
  while x>0:
    sum=x%10
    x=x//10
  return sum

max=-2147000000
for x in a:
  tot=digit_sum(x)
  if tot>max:
    max=tot
    res=x
print(res)