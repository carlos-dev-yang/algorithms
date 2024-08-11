from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string
from lib.TreeNode import TreeNode
from collections import defaultdict

class Solution:
    # copyFromLeetcodeDefLine
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dic = defaultdict(list)

        '''
        처음 문자열을 정렬해서 dictionary의 키로 만들고, 해당 키에 일치하는 애들은 그 키의 리스트에 계속 더함
        초반에 각 문자열별로 dict를 사용하는 방식을 썼는데 속도가 너무 느림
        '''
        for s in strs:
            sorted_str = ''.join(sorted(s))
            anagram_dic[sorted_str].append(s)
        
        return list(anagram_dic.values())


        
          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        (["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ]
    
    print("테스트 실행:")
    # change method of solution
    run_tests(solution.groupAnagrams, test_cases)