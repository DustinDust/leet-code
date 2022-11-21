from queue import Queue, LifoQueue as Stack


class TreeNode:
    left_child: "TreeNode"
    right_child: "TreeNode"
    val: any

    def __init__(self, val, left: "TreeNode" = None, right: "TreeNode" = None) -> None:
        self.val = val
        self.left_child = left
        self.right_child = right


def pre_traverse(root: TreeNode):
    if root is None:
        return
    print(root.val)
    pre_traverse(root.left_child)
    pre_traverse(root.right_child)


def in_traverse(root: TreeNode):
    if root is None:
        return
    in_traverse(root.left_child)
    print(root.val)
    in_traverse(root.right_child)


def post_traverse(root: TreeNode):
    if root is None:
        return
    post_traverse(root.left_child)
    post_traverse(root.right_child)
    print(root.val)


tree = TreeNode(1)
tree.left_child = TreeNode(2)
tree.right_child = TreeNode(3)
tree.left_child.left_child = TreeNode(4)
tree.left_child.right_child = TreeNode(5)
tree.right_child.left_child = TreeNode(6)
tree.right_child.right_child = TreeNode(7)

print("__pre order")
pre_traverse(tree)
print("__in order")
in_traverse(tree)
print("__post order")
post_traverse(tree)
