from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        start = 0
        max_length = 0
        
        for i, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                """
                여기가 알고리즘의 핵심부분
                딕셔너리를 사용해서 해당 문자열이 가지는 마지막 인덱스를 저장
                이렇게 하면 문자열을 매번 수정하지 않고 해당 문자열의 인덱스를 바로 획득할 수 있음
                """
                start = char_index[char] + 1
            else:
                max_length = max(max_length, i - start + 1)
            
            char_index[char] = i
            
        
        return max_length
          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("dvdf", 3),
    ]
    
    print("테스트 실행:")
    # copyFromLeetcodeDefLine
    run_tests(solution.lengthOfLongestSubstring, test_cases)