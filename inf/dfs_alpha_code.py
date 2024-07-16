import sys
sys.stdin = open('dfs_alpha_code.txt', 'r')
A=list(map(int, input()))
n=len(A)

# print(chr(65))
chr_list=[]
ch=[]
cnt=0
def DFS(L):
  global cnt
  if L==n:
    for x in ch:
      print(chr(64+x), end='')
    print()
    cnt+=1
    return
  else: 
      ch.append(A[L])
      DFS(L+1)
      ch.pop()
      if L<n-1:
        val=(A[L]*10)+A[L+1]
        if val < 26:
          ch.append(val)
          DFS(L+2)
          ch.pop()

DFS(0)
print(cnt)