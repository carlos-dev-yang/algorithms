from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        tails = [0]*n
        size = 0

        '''
        오름차순 정렬이면 2진 트리가 가능함.
        '''
        for num in nums:
            left, right = 0, size

            while left < right:
                mid = (left + right) // 2
                if tails[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            tails[left] = num
            size = max(size, left + 1)
        
        return size

          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        ([10,9,2,5,3,7,4,101,18,1,2,3,4,5], 5),
        ([0,1,0,3,2,3], 4),
        ([7,7,7,7,7,7,7], 1),
    ]
    
    print("테스트 실행:")
    # copyFromLeetcodeDefLine
    run_tests(solution.lengthOfLIS, test_cases)