import sys
sys.stdin = open('biggest_number.txt', 'r')
a, n=input().split()
a=list(map(int, list(a)))
n=int(n)

stack=[]
for x in a:
  while stack and n>0 and stack[-1]<x:
    stack.pop()
    n-=1
  stack.append(x)
if n>0:
  stack=stack[:-n]

print(stack)