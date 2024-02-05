
1st

```python
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        new_node = None
        if not root2:
            new_node = TreeNode(root1.val)
            new_node.left = self.mergeTrees(root1.left, None)
            new_node.right = self.mergeTrees(root1.right, None)
        elif not root1:
            new_node = TreeNode(root2.val)
            new_node.left = self.mergeTrees(None, root2.left)
            new_node.right = self.mergeTrees(None, root2.right)
        else:
            new_node = TreeNode(root1.val + root2.val)
            new_node.left = self.mergeTrees(root1.left, root2.left)
            new_node.right = self.mergeTrees(root1.right, root2.right)

        return new_node
```

