from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string
from collections import defaultdict

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        
        '''
        floyd의 cycle detection을 사용하는데
        첫 번째 만나는 포인트가 사이클내에 중복이 있다는것을 의미함.
        두번째 while문에서는 각자 다른 출발점에서 시작해서 같은 속도로 나아가면 중복에서 항상 만나는다는 것임..
        어렵다
        수학 등식으로는 설명된다함 :sad
        '''

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow
                
          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        ([1,3,4,2,2], 2),
        ([3,1,3,4,2], 3),
        ([3,3,3,3,3], 3),
        ([1,5,3,7,6,3,2,4], 3),
    ]
    
    print("테스트 실행:")
    # copyFromLeetcodeDefLine
    run_tests(solution.findDuplicate, test_cases)