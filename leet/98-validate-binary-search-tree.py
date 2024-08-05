from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string
from lib.TreeNode import TreeNode

class Solution:
    # copyFromLeetcodeDefLine
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        '''
        이 validate 함수는 가장 상위 루트 노드부터 값의 유효성을 항상 검증하는 로직으로 되어있음
        왼쪽으로 뻗어나가는 건 이전 min 값을 유지하고, 현재 node값을 max로 대치함
        오른쪽으로 뻗어나가는 건 현재 node값을 min으로 전달하고 이전 max값을 유지함
        이렇게 함으로서 다음 노드는 현재 노드까지 충족된 조건을 그대로 이어받게 되고, 전체 노드가 완전하다는것을 검증함
        '''
        def validate(node: Optional[TreeNode], min_val: float = float('-inf'), max_val: float = float('inf')) -> bool:
            if not node:
                return True
            
            if node.val <= min_val or node.val >= max_val:
                return False
            
            return (validate(node.left, min_val, node.val)) and \
                (validate(node.right, node.val, max_val))
        
        return validate(root)
            

if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        ([2,1,3], True),
        ([5,1,4,None,None,3,6], False),
        ([1,None,1], False),
        ([5,4,6,None,None,3,7], False)
    ]
    
    print("테스트 실행:")
    # change method of solution
    run_tests(solution.isValidBST, test_cases)