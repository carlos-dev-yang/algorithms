from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 그래프 구성 (정방향)
        # 그래프 구현할때는 defaultdict를 이용해라. 없는 key에 접근해도 에러 없이 처리해준다.
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[course].append(pre)
        
        # 방문 상태: 0 = 미방문, 1 = 방문 중, 2 = 방문 완료
        visited = [0] * numCourses
        
        def dfs(course):
            if visited[course] == 1:
                return False  # 순환 발견
            if visited[course] == 2:
                return True   # 이미 방문 완료
            
            visited[course] = 1  # 방문 중 표시
            
            for pre in graph[course]:
                if not dfs(pre):
                    return False
            
            visited[course] = 2  # 방문 완료 표시
            return True
        
        # 모든 과목에 대해 DFS 실행
        for course in range(numCourses):
            if visited[course] == 0:
                if not dfs(course):
                    return False
        
        return True


if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        ((2, [[1,0]]), True),
        ((2, [[1,0], [0,1]]), False),
    ]
    
    print("테스트 실행:")
    # copyFromLeetcodeDefLine
    run_tests(solution.canFinish, test_cases)