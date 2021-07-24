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

def diameterOfBinaryTree_issac(root: TreeNode) -> int:
    def dfs(root:TreeNode, diameter=1) -> int:
        print(diameter, root)
        if root.left is None and root.right is None:
            return diameter
        diameter_left = diameter
        diameter_right = diameter
        if root.left is not None:
            diameter_left += dfs(root.left, diameter_left)
        if root.right is not None:
            diameter_right += dfs(root.right, diameter_right)
        if diameter_left < diameter_right:
            diameter = diameter_right
        else:
            diameter = diameter_left
        return diameter

    diameter = 0
    if root.left is not None:
        diameter += dfs(root.left)
    if root.right is not None:
        diameter += dfs(root.right)
    return diameter


root = TreeNode(1)
root.add(2)
print(diameterOfBinaryTree_issac(root))