import random

class RandomizedSet:

    def __init__(self):
        self.arr = set()

    def insert(self, val: int) -> bool:
        if val not in self.arr:
            self.arr.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.arr:
            self.arr.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(tuple(self.arr))