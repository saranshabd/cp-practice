
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

    def inorder_traversal(self) -> None:
        self.__inorder_traversal(self.root)
        print()

    def __inorder_traversal(self, rootnode: TreeNode) -> None:
        if rootnode is None:
            return
        self.__inorder_traversal(rootnode.left)
        print(rootnode.key, end=' ')
        self.__inorder_traversal(rootnode.right)

    def delete_node(self, key: int) -> None:
        self.root = self.__delete_node(self.root, None, key)

    def __delete_node(self, rootnode: TreeNode, parentnode: TreeNode, key: int) -> TreeNode:
        if rootnode is None:
            return None

        if key < rootnode.key:
            rootnode.left = self.__delete_node(rootnode.left, rootnode, key)
        elif key > rootnode.key:
            rootnode.right = self.__delete_node(rootnode.right, rootnode, key)
        else:
            if rootnode.left is None:
                rootnode = rootnode.right
            elif rootnode.right is None:
                rootnode = rootnode.left
            else:
                ancestor_parent: TreeNode = self.__get_ancestor_parent(rootnode)
                if ancestor_parent == rootnode:
                    rootnode.left.right = rootnode.right

                    if parentnode is None:
                        self.root = rootnode.left
                    elif rootnode == parentnode.left:
                        parentnode.left = rootnode.left
                    else:
                        parentnode.right = rootnode.right
                    
                    rootnode = rootnode.left
                
                else:
                    ancestor_parent.right.left = rootnode.left
                    ancestor_parent.right.right = rootnode.right

                    if parentnode is None:
                        self.root = ancestor_parent.right
                    elif rootnode == parentnode.left:
                        parentnode.left = ancestor_parent.right
                    else:
                        parentnode.right = ancestor_parent.right
                    
                    rootnode = ancestor_parent.right
                    ancestor_parent.right = None
        
        return rootnode

    def __get_ancestor_parent(self, rootnode: TreeNode) -> TreeNode:
        ancestor = rootnode.left
        parent = rootnode
        while ancestor.right is not None:
            parent = ancestor
            ancestor = ancestor.right
        return parent
