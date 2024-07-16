import sys
sys.stdin = open('dice_game.txt', 'r')
n=int(input())
winner=0

for i in range(n):
  tmp=list(map(int, input().split()))

  dice_map=[0] * 7
  for x in tmp:
    dice_map[x] += 1
  max=0
  price=0
  for index, val in enumerate(dice_map):
    if val==3:
      price=10000+(index*1000)
      break
    if val==2:
      price=1000+(index*100)
      break
    if val==1:
      if max<index:
        max=index
  else:
    price=max*100
  
  if winner<price:
    winner=price
print(winner)