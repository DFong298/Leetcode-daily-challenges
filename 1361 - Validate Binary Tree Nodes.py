class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        node_set = set(range(n))
        childs_set = set(leftChild + rightChild)
        if -1 in childs_set:
            childs_set.remove(-1)

        parent = node_set - childs_set
        if len(parent) != 1:
            return False

        p = parent.pop()

        def dfs(u):
            if u == -1:
                return True
            if u in visited:
                return False
            visited.add(u)
            return dfs(leftChild[u]) and dfs(rightChild[u])

        visited = set()
        if not dfs(p): return False
        if len(visited) != n:
            return False

        return True
