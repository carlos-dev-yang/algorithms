from typing import List, Tuple, Any, Callable, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 리스트를 연결 리스트로 변환하는 유틸리티 함수
def create_linked_list(elements: list) -> Optional[ListNode]:
    dummy = ListNode(0)
    current = dummy
    for element in elements:
        current.next = ListNode(element)
        current = current.next
    return dummy.next

# 연결 리스트를 문자열로 변환하는 유틸리티 함수
def linked_list_to_string(head: Optional[ListNode]) -> str:
    elements = []
    current = head
    while current:
        elements.append(str(current.val))
        current = current.next
    return ' -> '.join(elements)

def list_to_linked_list(lst: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# 사용 예시
if __name__ == "__main__":
    # 리스트를 연결 리스트로 변환
    numbers = [1, 2, 3, 4, 5]
    linked_list = create_linked_list(numbers)
    
    # 연결 리스트 출력
    print(linked_list_to_string(linked_list))  # 출력: 1 -> 2 -> 3 -> 4 -> 5