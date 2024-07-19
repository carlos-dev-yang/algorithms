# ListNode 정의
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val    # 노드의 값
        self.next = next  # 다음 노드를 가리키는 참조

# 1. 단일 노드 생성
node1 = ListNode(1)
print(f"단일 노드: 값 = {node1.val}, 다음 노드 = {node1.next}")

# 2. 여러 노드를 연결하여 리스트 만들기
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
print("\n여러 노드 연결:")
print(f"node1: 값 = {node1.val}, 다음 노드 값 = {node1.next.val}")
print(f"node2: 값 = {node2.val}, 다음 노드 값 = {node2.next.val}")
print(f"node3: 값 = {node3.val}, 다음 노드 = {node3.next}")

testNode = ListNode(1)
testNode.next = ListNode(2)
testNode2 = ListNode(4)
testNode2.next = ListNode(5)
testNode2.next = testNode

def test(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print('None')

test(testNode2)
    


# 3. 연결 리스트 순회
def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

print("\n연결 리스트 순회:")
print_list(node1)

# 4. 리스트의 끝에 노드 추가
def append_node(head, val):
    new_node = ListNode(val)
    if not head:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

node1 = append_node(node1, 4)
print("\n노드 추가 후 연결 리스트:")
print_list(node1)

# 5. 리스트의 특정 위치에 노드 삽입
def insert_node(head, val, position):
    new_node = ListNode(val)
    if position == 0:
        new_node.next = head
        return new_node
    current = head
    for _ in range(position - 1):
        if not current:
            return head
        current = current.next
    if current:
        new_node.next = current.next
        current.next = new_node
    return head

node1 = insert_node(node1, 5, 2)
print("\n노드 삽입 후 연결 리스트:")
print_list(node1)

# 6. 리스트에서 노드 제거
def remove_node(head, val):
    if not head:
        return None
    if head.val == val:
        return head.next
    current = head
    while current.next:
        if current.next.val == val:
            current.next = current.next.next
            return head
        current = current.next
    return head

node1 = remove_node(node1, 3)
print("\n노드 제거 후 연결 리스트:")
print_list(node1)

# 7. 리스트 뒤집기
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_temp = current.next
        current.next = prev
        prev = current
        current = next_temp
    return prev

reversed_list = reverse_list(node1)
print("\n리스트 뒤집기 후:")
print_list(reversed_list)