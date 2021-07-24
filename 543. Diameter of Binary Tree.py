import collections


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        self.level_queue = collections.deque()

    def add(self, val):
        if self.left is None:
            self.left = TreeNode(val)
            self.level_queue.append(self.left)
        elif self.right is None:
            self.right = TreeNode(val)
            self.level_queue.append(self.right)
        else:
            tmp_node = self.level_queue[0]
            tmp_node.add(val)
            if tmp_node.left is not None and tmp_node.right is not None:
                self.level_queue.popleft()

    def __str__(self):
        return str(self.val)


def diameterOfBinaryTree_online(root: TreeNode) -> int:
    result = 0
    def dfs(root: TreeNode):
        nonlocal result
        if root is None:
            return -1
        left = dfs(root.left)
        right = dfs(root.right)
        result = max(result, left + right + 2)
        return 1 + max(left, right)

    dfs(root)
    return result


root = TreeNode(1)
root.add(2)
root.add(3)
root.add(4)
root.add(5)
root.add(6)
print(diameterOfBinaryTree_online(root))
