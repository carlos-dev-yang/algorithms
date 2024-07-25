from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n//2):
            for j in range(i, n - i - 1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = tmp
        return matrix

if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        ([[1,2,3],
          [4,5,6],
          [7,8,9]],
         [[7,4,1],
          [8,5,2],
          [9,6,3]]),
        ([[5,1,9,11],
          [2,4,8,10],
          [13,3,6,7],
          [15,14,12,16]], [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]),

    ]
    
    print("테스트 실행:")
    # copyFromLeetcodeDefLine
    run_tests(solution.rotate, test_cases)