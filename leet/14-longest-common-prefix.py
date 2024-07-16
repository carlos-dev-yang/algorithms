from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs=sorted(strs)
        first=strs[0]
        last=strs[-1]
        res=''
        for c1, c2 in zip(first, last):
            if c1==c2:
                res+=c1
            else:
                break
        return res
          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        (["flower","flow","flight"], 'fl'),
        (["dog","racecar","car"], ''),
        (["cir","car"], 'c')
    ]
    
    print("테스트 실행:")
    # copyFromLeetcodeDefLine
    run_tests(solution.longestCommonPrefix, test_cases)