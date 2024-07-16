import sys
sys.stdin = open('ten_to_two_recursive.txt', 'r')

def DFS(x):
  if x==0:
    return
  else:
    DFS(x//2)
    print(x%2, end='')

if __name__=="__main__":
  n=int(input())
  DFS(n)