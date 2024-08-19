from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string
from lib.TreeNode import TreeNode

class Solution:
    # copyFromLeetcodeDefLine
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        리트코드의 문제는 정상적으로 동작하지 않음. 솔루션에 문제가 있어보임
        lca - 가장 가까운 공통 조상을 찾는 문제로
        p와 q가 같은 조상을 가진다면, left와 right가 동시에 존재할때 rt를 return하는것으로 lca가 판명되고
        끝까지 가도 둘 중에 하나만 return이 된다면, p나 q하나는 찾아낸 노드의 하위에 있다고 보기 때문에 마지막 조건
        return left if left is not None else right로
        왼쪽과 오른쪽 하나만 있을때 해당 노드를 lca로 인정하게 됨.
        '''
        def search(rt: 'TreeNode'):
            if rt is None or rt.val == p or rt.val == q:
                return rt

            left = search(rt.left)
            right = search(rt.right)

            if left is not None and right is not None:
                return rt
            
            return left if left is not None else right
        
        res = search(root)
        return res.val
          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        (([3,5,1,6,2,0,8,None,None,7,4], 5, 1), 3),
        (([3,5,1,6,2,0,8,None,None,7,4], 5, 4), 5),
        (([1,2], 1, 2), 1),
    ]
    
    print("테스트 실행:")
    # change method of solution
    run_tests(solution.lowestCommonAncestor, test_cases)