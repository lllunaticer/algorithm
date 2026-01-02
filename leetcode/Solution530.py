from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 中序遍历二叉查找树的结果有序，有序数组中相邻元素之差产生最小差分
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = inf
        before = -inf

        # 中序遍历
        def dfs(root: Optional[TreeNode]):
            if root is None:
                return
            dfs(root.left)
            nonlocal res, before
            res = min(res, abs(before - root.val))
            before = root.val
            dfs(root.right)

        dfs(root)
        return res
