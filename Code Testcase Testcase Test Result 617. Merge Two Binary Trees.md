
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

> 1st は、私は return new_node 3回書いちゃいます。

2nd
```python
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        if not root2:
            return copy.deepcopy(root1)
        if not root1:
            return copy.deepcopy(root2)
        merged_node = TreeNode(root1.val + root2.val)
        merged_node.left = self.mergeTrees(root1.left, root2.left)
        merged_node.right = self.mergeTrees(root1.right, root2.right)
        return merged_node
```

final
```python
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 and not root2:
            return None
        if not root1:
            return root2
        if not root2:
            return root1
        new_node = TreeNode(root1.val + root2.val)
        new_node.left = self.mergeTrees(root1.left, root2.left)
        new_node.right = self.mergeTrees(root1.right, root2.right)
        return new_node
```

4th

破壊的
```python
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)
        return root1
```

非破壊的

https://docs.python.org/3/library/copy.html#copy.deepcopy
> A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found in the original.

`copy.deepcopy`だとノードを再帰的にたどって複製してくれる。

```python
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return copy.deepcopy(root2)
        if root2 is None:
            return copy.deepcopy(root1)
        node = TreeNode(root1.val + root2.val)
        node.left = self.mergeTrees(root1.left, root2.left)
        node.right = self.mergeTrees(root1.right, root2.right)
        return node
```
