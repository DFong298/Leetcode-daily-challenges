class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # adj list
        adj = [[] for _ in range(n)]
        for u, v in relations:
            adj[v-1].append(u-1) # reversed edges

        # top sort
        st = []
        vis = [False]*n

        def topsort(u):
            vis[u] = True
            for v in adj[u]:
                if not vis[v]:
                    topsort(v)
            st.append(u)

        for i in range(n):
            if not vis[i]:
                topsort(i)

        # Algo
        distTo = time.copy()

        for i in st:
            if adj[i]:
                distTo[i] = time[i] + max([distTo[j] for j in adj[i]])
            else:
                distTo[i] = time[i]
        
        return max(distTo)
