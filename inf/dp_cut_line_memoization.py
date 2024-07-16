import sys
sys.stdin = open('decide_stall.txt', 'r')

def DFS(len):
  if dy[len]>0:
    return dy[len]
  if len==1 or len==2:
    return len
  
  dy[len]=DFS(len-1)+DFS(len-2)
  return dy[len]
      

n=50
dy=[0]*(n+1)

print(DFS(n))
