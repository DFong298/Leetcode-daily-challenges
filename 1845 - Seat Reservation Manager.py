class SeatManager:

    def __init__(self, n: int):
        self.max = 0
        self.pq = []

    def reserve(self) -> int:
        if self.pq:
            return heappop(self.pq)
        self.max += 1
        return self.max

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.pq, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)