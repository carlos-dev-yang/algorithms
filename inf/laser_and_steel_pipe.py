import sys
sys.stdin = open('laser_and_steel_pipe.txt', 'r')
a=list(input())

stack=[]

last=''
cnt=0
for x in a:
  if x=='(':
    stack.append(x)
  else:
    stack.pop()
    if last=='(':
      cnt+=len(stack)
    else:
      cnt+=1
  last=x

print(cnt)
    