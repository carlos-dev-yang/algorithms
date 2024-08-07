from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string
from lib.TreeNode import TreeNode

class Solution:
    # copyFromLeetcodeDefLine
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
        
        m, n = len(matrix), len(matrix[0])
        result = []
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        r, c = 0, 0

        '''
        방향을 하나씩 막고 다음 방향에 따라서 값을 재할당 하는 방식을 노가다라고 생각하지 말자..
        r, c에 값을 할당할 때 nr, nc를 한 번 계산했다고 다시 계산하는게 이상하다는 생각으로 한참 시간낭비 함.
        처음에는 단순하게 해결보고, 그 다음에 개선하는 방식을 취해보자.. 동작이 우선임
        '''
        for _ in range(m * n):
            result.append(matrix[r][c])
            matrix[r][c] = '#'

            nr, nc = r + directions[d][0], c + directions[d][1]
            if 0 <= nr < m and 0 <= nc < n and matrix[nr][nc] != '#':
                r, c = nr, nc
            else:
                d = (d + 1) % 4
                r, c = r + directions[d][0], c + directions[d][1]
        
        return result
        
            
        
          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        ([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,6,9,8,7,4,5]),
        ([[1,2,3,4],[5,6,7,8],[9,10,11,12]], [1,2,3,4,8,12,11,10,9,5,6,7]),
    ]
    
    print("테스트 실행:")
    # change method of solution
    run_tests(solution.spiralOrder, test_cases)