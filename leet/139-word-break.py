from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string

class Solution:
    # copyFromLeetcodeDefLine
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False]*(n + 1)
        dp[0] = True

        '''
        단어를 한 단어씩 분해해서 해당 위치별로 단어가 완성되는지 기록함
        cat sand 같은 단어의 완성을 위해서 앞에서부터 조합이 가능한 단어의 위치에는 True로 체크함
        i배열로 한 글자씩 추가하면서 단어 검사를 하고, j배열로 앞에서부터 한 글자씩 제거하면서 
        앞에 단어 + 뒤에 단어 조합으로 단어가 완성 가능한지 체크한다.
        단어 위치에 True 표시가 되어있는 경우 해당 위치까지는 단어가 완성 가능함을 의미하므로
        j지점 부터 현재 단어의 끝부분 i까지의 단어만 사전에 있으면 해당 단어는 완성이 가능하다고 본다. 
        '''
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[n]
          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        (("leetcode", ["leet","code"]), True),
        (("catsandog", ["cats","dog","sand","and","cat"]), False),
        (("catsandog", ["og","cats","dog","sand","and","cat"]), True),
        (("applepenapple", ["apple","pen"]), True),
    ]
    
    print("테스트 실행:")
    # change method of solution
    run_tests(solution.wordBreak, test_cases)