from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        carry=0
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            total = x + y + carry
            carry = total // 10
            
            cur.next = ListNode(total % 10)
            cur = cur.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

          
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [  
        (([2,4,3], [5,6,4]), [7,0,8]),
        (([0], [0]), [0]),
        (([9,9,9,9,9,9,9], [9,9,9,9]), [8,9,9,9,0,0,0,1]),
    ]
    
    print("테스트 실행:")
    # copyFromLeetcodeDefLine
    run_tests(solution.addTwoNumbers, test_cases)