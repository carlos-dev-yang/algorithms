from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string
from lib.TreeNode import TreeNode

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        res = [0] * n
        stack = []

        '''
        리스트에 있는 나보다 큰 값이나 작은값들을 비교할때는, 스택을 활용하면 수월하게 비교가 가능함
        나보다 작은값이 있는지 스택에서 확인해서 있으면 다 꺼내서 해당 값들을 설정해주고,스택을 비울 수 없으면
        자기 자신이 스택에 들어가면 문제가 가볍게 해결 됨.
        그냥 단순하게 푸는것은 O(n^2)이고 스택을 활용하면 O(n)이 된다.
        '''
        for i, temperature in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temperature:
                last_index = stack.pop()
                res[last_index] = i - last_index

            stack.append(i)
        
        return res
          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        ([73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0]),
        ([30,40,50,60], [1,1,1,0]),
        ([30,60,90], [1,1,0]),
    ]
    
    print("테스트 실행:")
    # change method of solution
    run_tests(solution.dailyTemperatures, test_cases)