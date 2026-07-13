class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[str]
        """

        res = []

        def dfs(node, path):
            if node is None:
                return

            path += str(node.val)

            if node.left is None and node.right is None:
                res.append(path)
                return

            path += "->"

            dfs(node.left, path)
            dfs(node.right, path)

        dfs(root, "")

        return res
