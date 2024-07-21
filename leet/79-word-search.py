from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string
from collections import defaultdict

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        # 커팅 하는방식은 상위 속도의 답변을 확인해서 가져옴
        # 문자열 길이가 전체 단어의 길이 합을 넘어가면 즉시 중단
        if len(word) > m * n:
            return False

        # 단어별로 갯수를 확인
        counter = defaultdict(int)
        for i in range(m):
            for j in range(n):
                counter[board[i][j]] += 1
        
        # 시작 단어와 끝 단어의 빈도를 비교해서 시작단어가 더 많으면 문자열을 뒤집음
        # 진입점이 적을수록 DFS를 최대한 덜 호출하기 때문
        if counter[word[0]] > counter[word[-1]]:
            word = word[::-1]

        # 정답의 문자열 갯수만큼 보드에 존재하는지 확인, 한가지라도 갯수가 미달이라면 dfs 태울필요도 없음.
        for char in word:
            print(char, counter[char])
            if counter[char] == 0:
                return False
            counter[char] -= 1

        def dfs(i, j, k):
            if k == len(word):
                return True
            
            # 현재 좌표가 정상적인지 확인하고 좌표의 단어가 워드의 현재 탐색 대상 문자열인지 확인하는 작업
            if (i < 0 or i >= m or j < 0 or j >= n or 
                board[i][j] != word[k]):
                return False
            
            temp = board[i][j]
            board[i][j] = '#'
            
            result = (dfs(i+1, j, k+1) or dfs(i-1, j, k+1) or
                      dfs(i, j+1, k+1) or dfs(i, j-1, k+1))
                
            board[i][j] = temp
            return result

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        
        return False
          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기,
        # 출력이 여러개이면 리스트로 묶기
        (([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCCED'), True),
        (([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'SEE'), True),
        (([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'ABCB'), False),
    ]
    
    print("테스트 실행:")
    # copyFromLeetcodeDefLine
    run_tests(solution.exist, test_cases)