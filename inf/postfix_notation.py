import sys
sys.stdin = open('postfix_notation.txt', 'r')
a=list(input())

stack=[]
res=''
for x in a:
  if x.isdecimal():
    res+=x
  else:
    if x=='(':
      stack.append(x)
    elif x=='*' or x=='/':
      while stack and (stack[-1]=='*' or stack[-1]=='/'):
        res+=stack.pop()
      stack.append(x)
    else:
      while stack and (stack[-1]!='('):
        res+=stack.pop()
        
      if x==')':
        stack.pop()
      else:
        stack.append(x)

for r in stack:
  res+=r

print(res)