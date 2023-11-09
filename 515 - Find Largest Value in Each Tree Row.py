# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return None
        res = []
        q = deque()
        q.append(root)
        while q:
            mx = -float('inf')
            for i in range(len(q)):
                node = q.popleft()
                mx = max(mx, node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            res.append(mx)
        return res
