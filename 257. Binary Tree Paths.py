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

def binaryTreePaths_issac(root):
    array = []
    if root.val is None:
        return array
    string = str(root.val)
    if root.left is None and root.right is None:
        array.append(string)
    if root.left is not None:
        preorder(root.left, array, string)
    if root.right is not None:
        preorder(root.right, array, string)
    return array

def preorder(node, array, string):
    string += f"->{node.val}"
    if node.left is None and node.right is None:
        array.append(string)
    if node.left is not None:
        preorder(node.left, array, string)
    if node.right is not None:
        preorder(node.right, array, string)
    return string


root = TreeNode(1)
root.add(2)
root.add(3)
root.add(None)
root.add(5)
print(binaryTreePaths_issac(root))