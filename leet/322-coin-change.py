from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount + 1
        MAX = n
        dp = [MAX] * n
        dp[0] = 0

        '''
        같은 동전을 여러개 사용할 수 있어서 dp로 해결할 수 있는 이 문제는
        초기 dp 배열을 명확하게 정의해야 문제해결이 가능함.
        초반에는 dp를 0으로 초기화 했는데, 0은 동전을 놓을 수 있다는 의미가 되니
        max값 (amount + 1)로 초기화를 해서 동전이 놓일 수 있는 부분들을 확인하도록 해야함.
        이 경우는 0부터 출발하는 동전 5의 위치는 0의 위치에 값이 0이라 min 코드에서 0 + 1 로 초기화 됨.
        이후부터는 실제 동전이 놓일 수 있는 위치에만 값을 갱신하도록 한다.
        '''
        for coin in coins:
            for i in range(coin, n):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != MAX else -1
          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        (([1,2,5], 11), 3),
        (([2], 3), -1),
        (([1], 0), 0),
        (([5], 8), -1),
    ]
    
    print("테스트 실행:")
    run_tests(solution.coinChange, test_cases)