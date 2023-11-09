class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        q = deque(arr)
        c = 0
        while c < k:
            if len(q) > 1:
                if q[0] > q[1]:
                    c += 1
                    q[0], q[1] = q[1], q[0]
                    q.popleft()
                else:
                    q.popleft()
                    c = 1
            else:
                return q[0]
        return q[0]