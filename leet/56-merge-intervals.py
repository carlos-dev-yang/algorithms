from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string
from collections import deque

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        # 결과값을 담을 배열
        merged = []
        for interval in intervals:
            # 처음 not merged 조건으로 그냥 merged에 초기값을 넣는다.
            # 이 행위로 처음에 빈 배열을 처리하기 위해서 코드가 이상하게 흘러가는걸 막는다.
            # 이후에는 merged의 마지막 배열값의 끝 값이 새로 들어오는 interval의 시작값보다 작으면 겹치지 않는다고 보고 새로운 값을 추가
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            # 겹친다고 하면 마지막 값을 방금 들어온 인터벌의 마지막 값으로 갱신하기
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        ([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
        ([[1,4],[4,5]], [[1,5]]),
    ]
    
    print("테스트 실행:")
    # copyFromLeetcodeDefLine
    run_tests(solution.merge, test_cases)