from lib.leetcode_tester import run_tests

class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not stack or \
                    (c== ')' and stack[-1] != '(') or \
                    (c== ']' and stack[-1] != '[') or \
                    (c== '}' and stack[-1] != '{'):
                    return False
                stack.pop()
        return not stack
          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ('([)]', False),
        (']', False),
        ('[([]])', False),
    ]
    
    print("테스트 실행:")
    # copyFromLeetcodeDefLine
    run_tests(solution.isValid, test_cases)