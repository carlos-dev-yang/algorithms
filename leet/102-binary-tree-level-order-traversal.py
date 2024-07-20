from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string
from lib.TreeNode import TreeNode

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        print(root)
        
          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        ([3,9,20,None,None,15,7], [[3],[9,20],[15,7]]),
        ([1], [1]),
        ([], []),
    ]
    
    print("테스트 실행:")
    # copyFromLeetcodeDefLine
    run_tests(solution.levelOrder, test_cases)