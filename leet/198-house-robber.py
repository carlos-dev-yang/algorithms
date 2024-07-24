from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # 2단계 전 까지만 비교하면 됨
        # 이전값과 비교해서 지금이 시원찮으면 훔치지 않으면 i-1과 i-2+current가 최적해가 됨
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return max(dp)
                

          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        ([1,2,3,1], 4),
        ([2,7,9,3,1], 12),
    ]
    
    print("테스트 실행:")
    # copyFromLeetcodeDefLine
    run_tests(solution.rob, test_cases)