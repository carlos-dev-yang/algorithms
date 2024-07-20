from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        '''
        흔한 전개방식을 가진 DFS 문제
        백트래킹만 잘 이용하면 큰 문제없이 닶을 전개할 수 있음
        '''
        def dfs(gens: List[int]):
            if len(gens) == len(nums):
                result.append(gens.copy())
            else:
                for x in nums:
                    if x not in gens:
                        gens.append(x)
                        dfs(gens)
                        gens.pop()
        
        dfs([])
        return result


          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        ([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
        ([0,1], [[0,1],[1,0]]),
        ([1], [[1]]),
    ]
    
    print("테스트 실행:")
    # copyFromLeetcodeDefLine
    run_tests(solution.permute, test_cases)