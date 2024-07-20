from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        max_height = max(height)

        '''
        이 문제는 단순한 투 포인터 기법으로 해결되는 문제긴 하지만
        input 값이 길어지는 경우 cutting을 아주 잘 해야속도나 메모리 사용량에서 잇점을 볼 수 있음
        현재 높이의 좌우를 비교하고 낮은 쪽 기준으로 width를 계산
        중간에 최대 높이와 남은 너비를 계산해봤을 때 현재 계산된 최대 아레아보다 작다면 더이상 수행하지 않는다.
        
        메모리를 극도로 줄이고 싶다면, 단순 두가지 값을 비교하는 min, max는 사용하지 않는게 좋다.
        '''
        while left < right:
            width = right - left

            if height[left] < height[right]:
                area = height[left] * width
                left += 1
            else:
                area = height[right] * width
                right -= 1

            max_area = max(max_area, area)

            if max_area >= max_height * width:
                break

        return max_area
        
          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        ([1,8,6,2,5,4,8,3,7], 49),
        ([1, 1], 1),
    ]
    
    print("테스트 실행:")
    # copyFromLeetcodeDefLine
    run_tests(solution.maxArea, test_cases)