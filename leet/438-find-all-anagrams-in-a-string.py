from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string
from lib.TreeNode import TreeNode
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def getIndex(char: str):
            return ord(char) - ord('a')

        n, m = len(s), len(p)
        if n < m:
            return []
        
        '''
        아나그램을 찾는 건 아나그램의 기준 값을 어떻게 해시화 하느냐가 중요한 것 같음
        일반적인 아스키 문자열이라면 26개의 배열로 비교하는게 가장 빠른 것 같고
        검색 대상이 되는 필드는 windowing을 해서 같은 값을 여러번 재생성 하지 않도록 한다.
        처음에 dictionary를 만들어서 비교하려고 했는데, 이 방법은 결국 너무 느려서..
        해시테이블을 직접 만들 수 있는지의 여부로 판가름 되는 것 같다.
        문자열은 항상 숫자로 변환할 수 있음을 잊지 않아야, 룰이 훨씬 간단해지는 것 같다.
        '''
        p_count = [0] * 26
        s_count = [0] * 26

        for char in p:
            p_count[getIndex(char)] += 1

        res = []
        for i in range(n):
            s_count[getIndex(s[i])] += 1

            if i >= m:
                s_count[getIndex(s[i - m])] -= 1

            if p_count == s_count:
                res.append(i - m + 1)

        return res
            
          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        (("cbaebabacd", 'abc'), [0, 6]),
        (("abab", 'ab'), [0,1,2]),
    ]
    
    print("테스트 실행:")
    # change method of solution
    run_tests(solution.findAnagrams, test_cases)