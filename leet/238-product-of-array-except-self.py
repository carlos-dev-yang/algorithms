from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string
from lib.TreeNode import TreeNode

class Solution:
    # copyFromLeetcodeDefLine
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        n = len(nums)
        result = [1] * n
        
        prefix_product = 1
        suffix_product = 1

        for i in range(n):
            result[i] *= prefix_product
            prefix_product *= nums[i]

            result[n-i-1] *= suffix_product
            suffix_product *= nums[n-1-i]

        return result

          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        ([1,2,3,4], [24,12,8,6]),
        ([-1,1,0,-3,3], [0,0,9,0,0]),
    ]
    
    print("테스트 실행:")
    # change method of solution
    run_tests(solution.productExceptSelf, test_cases)