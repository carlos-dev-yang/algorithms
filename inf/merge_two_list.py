import sys
sys.stdin = open('merge_two_list.txt', 'r')

n=int(input())
n_list=list(map(int, input().split()))
m=int(input())
m_list=list(map(int, input().split()))

arr=[]
p1=0
p2=0

while True:
  if (n_list[p1]>m_list[p2]):
    arr.append(m_list[p2])
    p2+=1
  else:
    arr.append(n_list[p1])
    p1+=1
  if (p1==n or p2==m):
    break

if p1==n:
  arr.extend(m_list[p2:])
else:
  arr.extend(n_list[p1:])

print(arr)