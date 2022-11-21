class TreeNode:
    left: "TreeNode"
    right: "TreeNode"
    val: any

    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right
