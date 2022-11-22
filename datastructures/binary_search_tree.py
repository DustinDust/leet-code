class TreeNode:
    left: "TreeNode"
    right: "TreeNode"
    val: any

    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def search(tree: TreeNode, val):
    if not tree or tree.val == val:
        return tree
    elif val > tree.val:
        return search(tree.left)
    else:
        return search(tree.right)


def insert(tree: TreeNode, val):
    # worst case scenario: this tree is completely skewed and you have to traverese the whole tree -> O(n)
    # if the tree is not skewed -> O(h) where h is the height of the tree -> the insert to the deepest leaf node
    if not tree:
        return TreeNode(val)
    if val > tree.val:
        tree.right = insert(tree.right, val)
    elif val < tree.val:
        tree.left = insert(tree.left, val)

    return tree


def nextInOrderNode(node: TreeNode) -> TreeNode:
    current = node.right
    if current is None:
        return current
    while current.left is not None:
        current = current.left
    return current


def delete(tree: TreeNode, val):
    if tree is None:
        return tree
    if val < tree.val:
        tree.left = delete(tree.left, val)
    elif val > tree.val:
        tree.right = delete(tree.right, val)

    else:
        # only one child: remove current node -> replace with that child node
        if tree.left is None:
            temp = tree.right
            tree = None
            return temp
        elif tree.right is None:
            temp = tree.left
            tree = None
            return temp
        # if both child: the replacement node should be the next one as regard to the inorder traversal
        # to not break the nature of BST
        # essential just find the smallest node that is greater than current node
        temp = nextInOrderNode(tree)
        tree.val = temp.val
        # because we replace the deleted node with the node following it in the order -> we need to actually
        # remove that node as well
        tree.right = delete(tree.right, temp.val)
    return tree


def inorder(root: TreeNode):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


tree = TreeNode(50)
tree = insert(tree, 10)
tree = insert(tree, 5)
tree = insert(tree, 20)
tree = insert(tree, 60)
tree = insert(tree, 70)
tree = insert(tree, 40)
tree = insert(tree, 90)
tree = insert(tree, 30)
tree = insert(tree, 15)
tree = insert(tree, 100)
tree = insert(tree, 75)
tree = insert(tree, 65)
tree = insert(tree, 55)
tree = insert(tree, 57)
tree = insert(tree, 45)
tree = insert(tree, 15)
tree = insert(tree, 2)
tree = insert(tree, 7)

inorder(tree)

tree = delete(tree, 70)
print("DELETED\n")
inorder(tree)
