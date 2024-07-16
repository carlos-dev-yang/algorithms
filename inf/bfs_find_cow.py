import sys
from collections import deque

sys.stdin = open('bfs_find_cow.txt', 'r')
s, e=map(int, input().split())

def min_step(S, E):
  visited = set([S])
  que = deque([(S, 0)])

  while que:
    current, moves = que.popleft()
    print(que)

    if current == E:
      print(moves)
      return moves
  
    for next_pos in (current+1, current-1, current+5):
      if next_pos not in visited and 0 < next_pos < 10000:
        visited.add(next_pos)
        que.append([next_pos, moves+1])

  return -1

min_step(s, e)
