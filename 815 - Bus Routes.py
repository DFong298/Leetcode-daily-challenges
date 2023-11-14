class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0

        stops = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stops[stop].append(i)

        q = deque()
        visStop = set()
        visBus = set()
        for bus in stops[source]:
            q.append(bus)
            visBus.add(bus)
        visStop.add(source)

        dep = 0
        while q:
            dep += 1
            for _ in range(len(q)):
                u = q.popleft()

                for stop in routes[u]:
                    if stop in visStop:
                        continue
                    visStop.add(stop)

                    if stop == target:
                        return dep

                    for v in stops[stop]:
                        if v not in visBus:
                            q.append(v)
                            visBus.add(v)

        return -1