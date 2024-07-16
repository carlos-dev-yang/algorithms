import sys
sys.stdin = open('postfix_calculate.txt', 'r')
a=list(input())
stack=[]
res=''
for x in a:
  if x.isdecimal():
    stack.append(int(x))
  else:
    p2=stack.pop()
    p1=stack.pop()

    if x=='+':
      stack.append(p1+p2)
    elif x=='-':
      stack.append(p1-p2)
    elif x=='*':
      stack.append(p1*p2)
    elif x=='/':
      stack.append(p1/p2)
res=stack.pop()
print(res)