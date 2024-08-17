from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string
from lib.TreeNode import TreeNode

class Solution:
    # copyFromLeetcodeDefLine
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, target, path):
            if target == 0:
                result.append(path[:])
                return
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, target - candidates[i], path)
                path.pop()
        
        result = []
        candidates.sort()
        backtrack(0, target, [])
        return result
                
          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        (([2,3,6,7], 7), [[2,2,3], [7]]),
        (([2,3,5], 8), [[2,2,2,2],[2,3,3],[3,5]]),
        (([2], 1), []),
    ]
    
    print("테스트 실행:")
    # change method of solution
    run_tests(solution.combinationSum, test_cases)