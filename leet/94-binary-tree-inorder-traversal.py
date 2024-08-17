from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string
from lib.TreeNode import TreeNode

class Solution:
    # copyFromLeetcodeDefLine
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def search(node: Optional[TreeNode]):
            if not node:
                return

            search(node.left)
            res.append(node.val)
            search(node.right)
        
        search(root)
        return res


if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        ([1,None,2,3], [1,3,2]),
        ([], []),
        ([1], [1]),
    ]
    
    print("테스트 실행:")
    # change method of solution
    run_tests(solution.inorderTraversal, test_cases)