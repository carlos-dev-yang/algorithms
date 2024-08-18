from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string
from lib.TreeNode import TreeNode

class Solution:
    # copyFromLeetcodeDefLine
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_length = 0

        '''
        set을 이용해서 중복을 제거한 다음 마지막 값을 꺼내서 거기부터 좌우로 확장해나감
        찾은값은 제거하고 카운트를 계속 늘려나가서 set을 다 비울때까지 반복함.
        전체를 한 번만 탐색하고 지우는데, 각 값에 접근하는건 set이므로 o(1) 복잡도가 나옴
        따라서 전체를 반복하면 o(n) 복잡도임
        '''
        while num_set:
            num = num_set.pop()
            current_min = num - 1
            current_max = num + 1
            while current_min in num_set:
                num_set.remove(current_min)
                current_min -= 1

            while current_max in num_set:
                num_set.remove(current_max)
                current_max += 1

            max_length = max(max_length, current_max - current_min - 1)
        
        return max_length
          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        ([100,4,200,1,3,2], 4),
        ([0,3,7,2,5,8,4,6,0,1], 9),
    ]
    
    print("테스트 실행:")
    # change method of solution
    run_tests(solution.longestConsecutive, test_cases)