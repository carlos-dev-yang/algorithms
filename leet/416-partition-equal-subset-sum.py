from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string
from lib.TreeNode import TreeNode

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        
        target_sum = total_sum // 2

        '''
        저장되는 dp의 값이 꼭 입력 배열의 길이와 일치할필요가 없음
        초반에 dp에 각 배열의 인덱스에 맞춰 가능한 계산 결과를 다 저장했는데, 그럴필요가 없었음
        이건 종이에 적으면서 계산할때도 의문을 가졌던 부분인데 애매하게 넘어가서 set을 사용하는 걸 생각하지 못함.
        dp는 중복 계산을 방지하기 위한것이므로 각 과정에 맞는 값이 잘 저장될 수 있는 구조가 필요함
        이 문제의 경우는 일부 값이 target_sum과 일치되는지만 보면 되고,
        set에 계속 저장해도 중복되는 값을 저장되지 않으니 불필요한 메모리 낭비가 되진 않음
        '''
        dp = {0}

        for num in nums:
            new_sums = set()
            for current_num in dp:
                new_sum = current_num + num
                if new_sum == target_sum:
                    return True
                if new_sum < target_sum:
                    new_sums.add(new_sum)
            dp.update(new_sums) 

        return False

          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        ([1,5,11,5], True),
        ([1,2,3,5], False),
        ([1,1], True),
        ([14,9,8,4,3,2], True),
        ([100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97], False),
    ]
    
    print("테스트 실행:")
    # change method of solution
    run_tests(solution.canPartition, test_cases)