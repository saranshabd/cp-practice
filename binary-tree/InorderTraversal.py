
class TreeNode:
    def __init__(self, key: int) -> TreeNode:
        self.key: int = key
        self.left: TreeNode = None
        self.right: TreeNode = None


class BSTSolver:
    def __init__(self) -> BSTSolver:
        self.root: TreeNode = None

    def add_node(self, key: int) -> None:
        self.root = self.__add_node(self.root, key)

    def __add_node(self, rootnode: TreeNode, key: int) -> TreeNode:
        if rootnode is None:
            return TreeNode(key)
        if key < rootnode.key:
            rootnode.left = self.__add_node(rootnode.left, key)
        else:
            rootnode.right = self.__add_node(rootnode.right, key)
        return rootnode

    def inorder_traversal_with_recursion(self) -> None:
        self.__inorder_traversal_with_recursion(self.root)
        print()

    def __inorder_traversal_with_recursion(self, rootnode: TreeNode) -> None:
        if rootnode is None:
            return
        self.__inorder_traversal_with_recursion(rootnode.left)
        print(rootnode.key, end=' ')
        self.__inorder_traversal_with_recursion(rootnode.right)
    
    def inorder_traversal_iterative(self) -> None:
        currnode: TreeNode = self.root
        stack: list = []
        while currnode is not None:
            stack.append(currnode)
            currnode = currnode.left

        while len(stack) > 0:
            currnode: TreeNode = stack.pop()
            print(currnode.key)

            currnode = currnode.right
            while currnode is not None:
                stack.append(currnode)
                currnode = currnode.left

        print()
