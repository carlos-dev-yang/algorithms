from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string
from lib.TreeNode import TreeNode

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        dp = [[0] * n for _ in range(n)]

        '''
        2차원 배열에서 ii의 위치는 각 문자열의 시작점과 동일함
        '''
        for i in range(n):
            dp[i][i] = 1

        '''
        0,1/1,2/.../n-1,n 으로 진행하고
        0,2/1,3/.../n-2,n 
        .../0,n 까지 진행하면서 그 사이값을 구해둘 수 있음
        1,4를 검사했을때 s[1]==s[4] 라면 그 사이값 2,3에 있는 문자열은 이미 팰린드롬 수열 계산이 끝난 상태고
        그 값에서 + 2를 하면 현재 문자열의 팰린드롬 수열 길이를 나타냄
        사이값 2, 3의 위치가 i+1, j-1의 위치로 표현이 됨
        s[1]!=s[4]라면 사이값에 +2를 하지 않고, 지금까지 완성할 수 있는 가장 긴 팰린드롬 수열의 값을 가지게 됨
        이 부분이 max(dp[i+1][j], dp[i][j-1])로 표현된다.
        '''
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] == s[j] and length == 2:
                    dp[i][j] = 2
                elif s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][n-1]

                

          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        ("bbbab", 4),
        ("cbbdb", 3),
    ]
    
    print("테스트 실행:")
    # change method of solution
    run_tests(solution.longestPalindromeSubseq, test_cases)