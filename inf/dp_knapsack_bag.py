import sys
sys.stdin = open('dp_knapsack_bag.txt', 'r')
n, m=map(int, input().split())
dy=[0]*(m+1)

for i in range(n):
  w, v=map(int, input().split())
  for j in range(w, m+1):
    dy[j]=max(dy[j], dy[j-w]+v)

def knapsack(W, weights, values, n):
    dp = [[0 for x in range(W+1)] for x in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, W+1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    for x in dp:
       print(x)
    return dp[n][W]

weights = [3, 2, 1, 2, 1, 2]
values = [4, 3, 2, 3, 1, 2]
max_score = knapsack(10, weights, values, 6)
print(f"최대 점수: {max_score}")