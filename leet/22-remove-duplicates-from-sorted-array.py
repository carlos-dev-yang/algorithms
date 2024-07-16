from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        cnt=0
        for i in range(n-1, -1, -1):
            if nums[i]==nums[i-1]:
                nums.remove(nums[i])
                cnt+=1
        return len(nums)
          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ([1,1,2], 2),
        ([0,0,1,1,1,2,2,3,3,4], 5)
    ]
    
    print("테스트 실행:")
    # copyFromLeetcodeDefLine
    run_tests(solution.removeDuplicates, test_cases)