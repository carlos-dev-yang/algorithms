from typing import List, Optional, Callable
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_to_tree(nums: List[Optional[int]]) -> Optional[TreeNode]:
    if not nums:
        return None
    root = TreeNode(nums[0])
    queue = deque([root])
    i = 1
    while queue and i < len(nums):
        node = queue.popleft()
        if i < len(nums) and nums[i] is not None:
            node.left = TreeNode(nums[i])
            queue.append(node.left)
        i += 1
        if i < len(nums) and nums[i] is not None:
            node.right = TreeNode(nums[i])
            queue.append(node.right)
        i += 1
    return root

def tree_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result[-1] is None:
        result.pop()
    return result

def is_tree_input(func: Callable) -> bool:
    return any('TreeNode' in str(param) for param in func.__annotations__.values())
