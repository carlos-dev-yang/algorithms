from lib.leetcode_tester import run_tests
from typing import List, Dict, Tuple, Optional
from lib.ListNode import ListNode, create_linked_list, linked_list_to_string

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2
        return dummy.next

          
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        (([1,2,4], [1,3,4]), [1,1,2,3,4,4]),
        (([], []), []),
        (([], [0]), [0]),
    ]
    print("테스트 실행:")
    # copyFromLeetcodeDefLine
    run_tests(solution.mergeTwoLists, test_cases)