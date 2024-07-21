from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string
from lib.TreeNode import TreeNode
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
           return []
        
        queue = deque([root])
        result = []
        left_to_right = True

        while queue:
          level_size = len(queue)
          current_level = deque()

          for _ in range(level_size):
            node = queue.popleft()

            # 여기서 자꾸 뒤집어서 queue에 append하려고 했으니 문제가 복잡해짐. 여기서 none이 아닐때만 queue에 넣는것으로 추가 검사 필요없음
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            # 여기서 방향에 따라 값을 삽입하는 방향 바꾸기. 이거까지 고민은 했는데 앞에서 queue를 처리하는 과정에서 이걸 하려고 해서 막힘
            if left_to_right:
               current_level.append(node.val)
            else:
               current_level.appendleft(node.val)
          
          result.append(list(current_level))
          left_to_right = not left_to_right
        return result
          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        ([3,9,20,4,8,15,7], [[3],[20,9],[4,8,15,7]]),
        ([3,9,20,None,None,15,7], [[3],[20,9],[15,7]]),
        ([1], [[1]]),
        ([], []),
    ]
    
    print("테스트 실행:")
    # copyFromLeetcodeDefLine
    run_tests(solution.zigzagLevelOrder, test_cases)