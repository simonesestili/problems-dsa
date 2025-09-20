class Router:
    def __init__(self, limit):
        self.limit = limit
        self.qs = defaultdict(deque)
        self.q = deque()
        self.packets = set()

    def addPacket(self, src, dst, time):
        if (src, dst, time) in self.packets:
            return False
        self.qs[dst].append((src, dst, time))
        self.q.append((src, dst, time))
        self.packets.add((src, dst, time))
        if len(self.q) > self.limit:
            _, dst, _ = self.q.popleft()
            self.packets.remove(self.qs[dst].popleft())
        return True

    def forwardPacket(self):
        if not self.q:
            return []
        packet = self.q.popleft()
        self.qs[packet[1]].popleft()
        self.packets.remove(packet)
        return packet

    def getCount(self, dst, start, end):
        r = bisect_right(self.qs[dst], end, key=lambda p: p[2])
        l = bisect_left(self.qs[dst], start, key=lambda p: p[2])
        return r - l
