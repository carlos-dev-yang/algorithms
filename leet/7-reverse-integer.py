from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string

"""
10진수를 이용한 수학적 연산이 대부분의 경우에 명확함.
32비트 제한인지 64비트 제한인지 문제를 확인해서 가드하는 장치를 마련해둬야 함.
오버플로우를 고려해야 함.
2진수로 변환해서 비트 연산을 하는게 특수한 경우에서 효과가 조금 있을 수 있지만
복잡함에 비해 이득이 크게 없음.
"""
class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)

        while x != 0:
            # 끝자리를 옮기기 위해서 빼냄
            digit = x % 10
            # 끝자리를 한자리씩 앞으로 옮기는 작업
            result = result * 10 + digit
            # 빼냈던 끝자리를 제거하는 작업
            x //= 10

        # 32비트를 넘어가지 않도록 가드
        if result > 2**31 - 1 or result < -2**31:
            return 0
        
        return sign * result
          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        (123, 321),
        (-123, -321),
        (120, 21),
    ]
    
    print("테스트 실행:")
    # copyFromLeetcodeDefLine
    run_tests(solution.reverse, test_cases)