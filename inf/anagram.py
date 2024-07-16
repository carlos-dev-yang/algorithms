import sys
sys.stdin = open('anagram.txt', 'r')
a=input()
b=input()

p=dict()

for char in a:
  p[char]=p.get(char, 0)+1

for char in b:
  p[char]=p.get(char, 0)-1

for key, val in p.items():
  if val>0:
    print('NO')
    break
else:
  print('YES')