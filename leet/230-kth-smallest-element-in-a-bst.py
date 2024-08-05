from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string
from lib.TreeNode import TreeNode

class Solution:
    # copyFromLeetcodeDefLine
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current: Optional[TreeNode] = root

        '''
        이진트리의 특성상 가장 왼쪽 리프가 가장 작은 숫자라는것을 활용해야함.
        1. 왼쪽 트리만 골라서 스택에 추가. 끝까지 가면 그 수가 가장 작은수임
        2. 스택에서 팝 할때마다 k에서 1씩 차감. k가 0이되면 해당 노드가 그 값임
        3. 팝 하고 해당 노드의 오른쪽 리프가 있는지 확인. 있다면 아직 더 탐색할 하위값이 있다는 뜻임.
        4. 있으면 해당 트리부터 다시 1번을 반복함.
        5. 없으면 자동으로 다음 스택의 값으 팝 됨. 3~5 반복
        '''
        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            k -= 1

            if k == 0:
                return current.val
            
            current = current.right
        
        return None

          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        (([3,1,4,None,2], 1), 1),
        (([5,3,6,2,4,None,None,1], 3), 3),
    ]
    
    print("테스트 실행:")
    # change method of solution
    run_tests(solution.kthSmallest, test_cases)