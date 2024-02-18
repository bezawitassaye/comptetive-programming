class RecentCounter:
    def __init__(self):
        self.buffer = []
        self.counter = 0

    def ping(self, t: int) -> int:
        self.buffer.append(t)
        while self.buffer and self.buffer[0] < t - 3000:
            self.buffer.pop(0)
        return len(self.buffer)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)