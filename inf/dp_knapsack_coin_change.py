import sys
sys.stdin = open('dp_coin_change.txt', 'r')
n=int(input())
cl=list(map(int, input().split()))
tot=int(input())
dy=[1000]*(tot+1)
dy[0]=0

for i in range(n):
    for j in range(cl[i], tot+1, 1):
        dy[j]=min(dy[j-cl[i]]+1, dy[j])
    print(dy)

print(dy[tot])