import sys
sys.stdin = open('dfs_duplicate_line_number.txt', 'r')
input=sys.stdin.readline
n, m=map(int, input().split())

CH=[0]*m
cnt=0
def DFS(L, ch):
  global cnt
  if L==m:
    for j in range(m):
      print(ch[j], end=' ')
    print()
    cnt+=1
    return
  else:
    for i in range(1, n+1):
      ch[L]=i
      DFS(L+1, ch)


DFS(0, CH)
print(cnt)