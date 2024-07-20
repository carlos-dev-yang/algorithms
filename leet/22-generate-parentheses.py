from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        아주 쉬운 DFS문제임에도 전개방식 조건을 정확히 찾지 못해서 헤맨 문제
        이 문제의 조건을 여러개 특정할 수 있었으면 전개방식도 금방 찾았을 듯.
        DFS는 전개 조건을 찾는게 가장 중요한 열쇠 같다
        조건을 나열해보면
        1. 문자열은 n * 2일때 종료한다.
        2. 열림괄호의 갯수는 n개까지만 가능하다.
        3. 닫힘괄호는 열림괄호 갯수까지만 가능하다.
        '''
        def DFS(left, right, s):
            if len(s) == n * 2:
                result.append(s)
                return
            
            if left < n:
                DFS(left + 1, right, s + "(")
            
            if right < left:
                DFS(left, right + 1, s +")")

        result = []    
        DFS(0, 0, "")
        return result
          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        (3, ["((()))","(()())","(())()","()(())","()()()"]),
        (1, ["()"]),
    ]
    
    print("테스트 실행:")
    # copyFromLeetcodeDefLine
    run_tests(solution.generateParenthesis, test_cases)