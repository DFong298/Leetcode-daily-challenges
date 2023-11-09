# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def calc_avg(u):
            nonlocal ans
            if not u:
                return 0, 0
            a = u.val
            l, lc = calc_avg(u.left)
            r, rc= calc_avg(u.right)

            if (a + l + r) // (lc + rc + 1) == u.val:
                ans += 1
            return (a + l + r), (lc + rc + 1)

        calc_avg(root)
        return ans