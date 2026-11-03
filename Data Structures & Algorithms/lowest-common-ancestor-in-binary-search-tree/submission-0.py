# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs_path(self, root: TreeNode, target: TreeNode):
        stack = [(root, [root])]

        while stack:
            node, path = stack.pop()
            if node == target:
                return path
            if node.right:
                stack.append((node.right, path + [node.right]))
            if node.left:
                stack.append((node.left, path + [node.left]))
        return []

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return
        p_path = self.dfs_path(root, p)
        q_path = self.dfs_path(root, q)

        for a, b in zip(p_path, q_path):
            if a != b:
                break
            lca = a
        return lca