from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string
from lib.TreeNode import TreeNode
import math

class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        OPS = {'+', '-', '*', '/'}

        '''
        연산이 아주 단순해서 숫자는 stack에 다 집어넣고 부호를 만나면 계산해서 다시 넣고를 반복하면 됨
        token이 int인지를 검사하는 것 보다 token이 operator에 속하는지를 보는게 좀 더 편한방법처럼 느껴짐
        음수 때문에 int를 검사하는게 str의 기본 함수로는 검사가 안됨. 추가로 함수를 만드느니 operator만 검사하는게 낫다고 판단됨
        '''
        for token in tokens:
            if token in OPS:
                right_val = res.pop()
                left_val = res.pop()
                
            if token == '+':
                res.append(left_val + right_val)
            elif token == '-':
                res.append(left_val - right_val)
            elif token == '*':
                res.append(left_val * right_val)
            elif token == '/':
                res.append(int(left_val / right_val))
            else:
                res.append(int(token))
        return res[0]


if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # 입력이 여러개이면 튜플로 묶기, 
        # 출력이 여러개이면 리스트로 묶기
        (["2","1","+","3","*"], 9),
        (["4","13","5","/","+"], 6),
        (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22),
    ]
    
    print("테스트 실행:")
    # change method of solution
    run_tests(solution.evalRPN, test_cases)