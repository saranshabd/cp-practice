
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        return self.inorder_traversal(root, L, R)
    
    def inorder_traversal(self, rootnode: TreeNode, L: int, R: int) -> int:
        if rootnode is None:
            return 0
        
        left_sum: int = self.inorder_traversal(rootnode.left, L, R)
        
        if rootnode.val >= L and rootnode.val <= R:
            curr_sum: int = rootnode.val
        else:
            curr_sum: int = 0
        
        right_sum: int = self.inorder_traversal(rootnode.right, L, R)
        
        return left_sum + curr_sum + right_sum
