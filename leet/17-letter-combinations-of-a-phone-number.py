from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string

phone_keypad = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz"
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        
        l = len(digits)
        result = []
        '''
        전형적인 DFS 문제라서 전체 탐색이라 최적화 할 만한것도 없음.
        이 문제의 핵심은 각 숫자가 구성할 수 있는 노드를 전부 구성한 다음
        하위 노드에서도 구성할 수 있는 노드를 전부 구성해서 값을 더하며 밑으로 전달하면 됨
        최 하위 노드에서는 현재까지 전달된 값을 리스트에 추가하고 return함
        하위까지 구사한 노드의 값들을 백트래킹 하는 작업이 필요한가..?
        '''
        def DFS(L, prev):
            if L == l:
                result.append(prev)
                return

            keypad = phone_keypad[digits[L]]
            for x in keypad:
                DFS(L+1, prev+x)

        DFS(0, '')
        return result
          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
        ("", []),
        ("2", ["a", "b", "c"]),
    ]
    
    print("테스트 실행:")
    # copyFromLeetcodeDefLine
    run_tests(solution.letterCombinations, test_cases)