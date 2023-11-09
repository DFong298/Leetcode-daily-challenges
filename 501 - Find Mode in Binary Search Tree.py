# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counter = {}
        def dfs(u):
            if u.val not in counter:
                counter[u.val] = 0
            counter[u.val] += 1
            if u.left:
                dfs(u.left)
            if u.right:
                dfs(u.right)
        
        dfs(root)
        mx = max(counter.values())
        return [i for i in counter if counter[i] == mx]
        