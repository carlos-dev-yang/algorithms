from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ''
        current_number = 0

        '''
        스택을 통해서 일정 영역을 변환하는 작업들을 변환되는 룰에 맞춰서 알고리즘 조작을 잘 해줘야 함.
        복잡도를 O(n)으로 처리할 수 있는 문제이니 stack을 잘 활용하기
        '''
        for char in s:
            print(stack)
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char == '[':
                stack.append(current_string)
                stack.append(current_number)
                current_number = 0
                current_string = ''
            elif char == ']':
                num = stack.pop()
                prev_string = stack.pop()
                current_string = prev_string + current_string * int(num)
            else:
                current_string += char
        return current_string



          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        ('3[a]2[bc]', 'aaabcbc'),
        ('3[a2[c]]', 'accaccacc'),
        ('2[abc]3[cd]ef', 'abcabccdcdcdef'),
    ]
    
    print("테스트 실행:")
    run_tests(solution.decodeString, test_cases)