from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string

class Solution:
    # copyFromLeetcodeDefLine
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1

        '''
        pivot된 배열의 경우 특정 기준으로 pivot된 부분을 찾기보다
        mid를 기준으로 좌/우 어느쪽이 정렬된지 우선 확인해야만 target값이 mid보다 작거나 큰지 비교하는게 의미가 있음
        정렬된 부분을 알지 못 한 상태에서는 mid와 target만으로는 해당 값이 좌/우 어디에 있는지 알지 못하기 때문
        '''
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # 왼쪽이 정렬됨
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                print(nums[mid], target, nums[right])
                if nums[mid] < target <= nums[right]:
                    print('left')
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
        

        

          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        (([4,5,6,7,0,1,2], 0), 4),
        (([4,5,6,7,0,1,2], 3), -1),
        (([1], 0), -1),
        (([1,3,5], 5), 2),
        (([3,1], 1), 1),
    ]
    
    print("테스트 실행:")
    # change method of solution
    run_tests(solution.search, test_cases)