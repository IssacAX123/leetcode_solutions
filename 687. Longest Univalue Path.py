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


def longestUnivaluePath(root: TreeNode) -> int:
    res = 0
    def dfs(root: TreeNode):
        nonlocal res
        if root is None:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        if root.left is not None and root.val == root.left.val:
            left += 1
        if root.right is not None and root.val == root.right.val:
            right += 1
        res = max(res, left + right)
        return max(left, right)

    dfs(root)
    return res

root = TreeNode(5)
root.add(4)
root.add(5)
root.add(1)
root.add(1)
root.add(5)
print(longestUnivaluePath(root))