import sys
sys.stdin = open('ssirum_player.txt', 'r')
n=int(input())
player=[]
for i in range(n):
  h, w=map(int, input().split())
  player.append((h, w))

player.sort(key=lambda x: (x[1], x[0]))

print(player)

cnt=n
es, ew=0, 0
for i in range(n):
  s,w=player[i]
  for j in range(i+1, n):
    es, ew=player[j]
    print(s, es, w, ew)
    if s<es and w<ew:
      print('drop')
      cnt-=1
      break
  
print(cnt)