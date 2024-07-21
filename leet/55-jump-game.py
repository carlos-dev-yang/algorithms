from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        '''
        현재 위치에서 최대로 갈 수 있는 값을 갱신하면서 한 칸씩 증가시켰을 때
        마지막 max_reach의 값이 마지막 위치보다 크다면 가능하다고 볼 수 있음.
        '''
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= len(nums) - 1:
                return True
        return True
                

          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        ([2,3,1,1,4], True),
        ([3,2,1,0,4], False),
        ([3,2,2,0,4], True),
        ([0], True),
        ([0,2,1,0,4], False),
    ]
    
    print("테스트 실행:")
    # copyFromLeetcodeDefLine
    run_tests(solution.canJump, test_cases)