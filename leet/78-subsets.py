from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string

class Solution:
    # copyFromLeetcodeDefLine
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        subset = []

        '''
        1부터 1개씩 증가하는 for문이 이 알고리즘의 핵심인 듯
        값이 증가한상태로 for문을 전부 수행하고, pop 한 상태에서 다음걸 수행하는 동작으로 
        모든 수의 조합을 완성한다
        '''
        def backtrack(index):
            res.append(subset[:])

            for i in range(index, n):
                subset.append(nums[i])
                backtrack(i + 1)
                subset.pop()

        backtrack(0)
        return res

        


          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        ([1,2,3], [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
    ]
    
    print("테스트 실행:")
    # change method of solution
    run_tests(solution.subsets, test_cases)