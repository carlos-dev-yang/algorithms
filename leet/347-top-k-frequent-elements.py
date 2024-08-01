from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string
from collections import Counter
import heapq

class Solution:
    # copyFromLeetcodeDefLine
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        (([1,1,1,2,2,3], 2), [1,2]),
        (([1], 1), [1]),
    ]
    
    print("테스트 실행:")
    run_tests(solution.topKFrequent, test_cases)