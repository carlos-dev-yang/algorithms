from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string
from lib.TreeNode import TreeNode

class Solution:
    # copyFromLeetcodeDefLine
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]
        
        '''
        일반적인 배열을 이진 탐색하는 방식과 크게 다른게 없고 종료 조건만 다른 알고리즘임
        다른 이진 탐색의 경우는 값을 찾으면 바로 종료지만, 이 경우는 같은 값을 만나면 기록하고
        왼쪽으로 가서 시작점을 찾거나, 오른쪽으로 가서 종료지점을 찾거나 하는 두가지 행위가 추가됨.
        같은값을 만나면 항상 i에 기록해서 다른 탐색에서 비정상적으로 종료 되더라도 i는 리턴 되도록 하면 됨.
        '''
        def search_binary(leftBias: bool):
            left, right = 0, n-1
            i = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    i = mid
                    if leftBias:
                        right = mid - 1
                    else:
                        left = mid + 1
            return i
        return [search_binary(True), search_binary(False)]

            
          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        (([5,7,7,8,8,10], 8), [3,4]),
        (([5,7,7,8,8,10], 6), [-1,-1]),
        (([], 0), [-1,-1]),
    ]
    
    print("테스트 실행:")
    # change method of solution
    run_tests(solution.searchRange, test_cases)