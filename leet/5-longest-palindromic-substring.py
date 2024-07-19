from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        # 한 글자씩 확장하는데, 홀수와 짝수의 케이스를 같이 증가하면서 검사함
        # 중앙을 지나면서 현재까지 발견한 수가 남은 수의 최대 가능성보다 크다면 중단(컷) 시킬 수 있음
        start, end = 0, 0
        for i in range(len(s)):
            len1 = expand_around_center(i, i)
            len2 = expand_around_center(i, i + 1)
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]

        
        
        


          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ("babad", ['bab', 'aba']),
        ("cbbd", 'bb'),
        ("aaaaaaaaabaaabababababababbbab", ["ababababababa", "babababababab"])
    ]
    
    print("테스트 실행:")
    # copyFromLeetcodeDefLine
    run_tests(solution.longestPalindrome, test_cases)