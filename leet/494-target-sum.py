from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string
from lib.TreeNode import TreeNode
from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        '''
        계산된값을 효율적으로 관리하기 위해서 defaultdict를 사용
        안에서 key를 기준으로 해시테이블처럼 관리해줌
        '''
        dp_dict = defaultdict(int)
        dp_dict[0] += 1

        for num in nums:
            '''
            경우의수를 매번 다 계산할필요 없이 여기에서도 딕셔너리 형태로 저장하고 합치기만 하면
            dp_dict의 원활한 업데이트 가능
            '''
            tmp_dict = defaultdict(int)
            for current_sum, count in dp_dict.items():
                tmp_dict[current_sum+num] += count
                tmp_dict[current_sum-num] += count
            dp_dict = tmp_dict
        return dp_dict[target]

          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        (([1,1,1,1,1], 3), 5),
        (([1], 1), 1),
    ]
    
    print("테스트 실행:")
    # change method of solution
    run_tests(solution.findTargetSumWays, test_cases)