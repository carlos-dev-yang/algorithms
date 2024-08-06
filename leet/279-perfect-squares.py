from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string
from lib.TreeNode import TreeNode

class Solution:
    # copyFromLeetcodeDefLine
    def numSquares(self, n: int) -> int:
        # 제곱수를 계산하기전에 제곱근으로 범위를 특정하는게 도움이 됨
        square_nums = [i**2 for i in range(1, int(n**0.5) + 1)]
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        '''
        bottom-up 형태로 처리하면서 각 단계별로 조합의 값을 설정하고
        마지막 단계에서 dp의 마지막 값을 리턴함.
        이건 n이 많을경우 시간이 오래 걸리는데,
        라그랑주의 정리 - 어떤 자연수는 최대 4개의 제곱수의 합으로 이루어져있다.
        를 이용해서 수학적인 접근으로 dp를 사용하지 않을 수 있음
        1개 - n이 완전 제곱수인지 체크
        4개 - 4^a * (8k + 7)의 형태인경우 (수학적인 이해도 필요)
        2개 - n에서 제곱수를 뺀 다음에, 그 값이 제곱수인지 확인
        3개 - 이도저도 아니면 3개의 제곱수의 합이라고 함.
        # 1개 완전 제곱수 체크
        if int(n**0.5)**2 == n:
            return 1
        
        # 4개 - 4의 배수 * (8k + 7) 형태 체크
        while n % 4 == 0:
            n //= 4
        if n % 8 == 7:
            return 4
        
        # 2개 - 2개의 제곱수 합 체크
        for i in range(1, int(n**0.5) + 1):
            if int((n - i*i)**0.5)**2 == n - i*i:
                return 2
        
        # 위의 경우가 모두 아니라면 3을 반환
        return 3
        '''
        for i in range(1, n + 1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i-square] + 1)
        
        return dp[n]

          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        (12, 3),
        (13, 2),
        (4, 1),
    ]
    
    print("테스트 실행:")
    # change method of solution
    run_tests(solution.numSquares, test_cases)