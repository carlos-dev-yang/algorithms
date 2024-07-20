from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string
from lib.TreeNode import TreeNode
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level = []

            '''
            이 문제는 아주 단순한 BFS탐색으로
            queue를 통해서 레벨별 작업을 한 단위로 묶어서 하는것에 익숙해지기 위함처럼 보임
            한 번 사이즈를 측정하고 나면 그 사이즈의 작업이 끝날때까지는 한 레벨로 취급되고
            이미 사이즈가 정해져 있어서 큐에 얼마든지 추가(append)하더라도 문제가 없음
            '''
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)

        return result
        
        
          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        ([3,9,20,None,None,15,7], [[3],[9,20],[15,7]]),
        ([1], [[1]]),
        ([], []),
        ([4, 15, 17, 19, 31, 44, 42, 49, 57], [[4], [15, 17], [19, 31, 44, 42], [49, 57]]),
    ]
    
    print("테스트 실행:")
    # copyFromLeetcodeDefLine
    run_tests(solution.levelOrder, test_cases)