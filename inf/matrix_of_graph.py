import sys
sys.stdin = open('dfs_adj_matrix_of_graph.txt', 'r')
n, m=map(int, input().split())

line=[]
for _ in range(m):
  line.append(list(map(int, input().split())))

matrix=[[0]*(n) for _ in range(n)] 

for l in line:
  matrix[l[0]-1][l[1]-1]=l[2]

for _ in matrix:
  print(_)