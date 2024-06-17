import random


class RandomizedSet:
    # HashMap + Array
    def __init__(self):
        self.hashMap = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.hashMap:
            return False

        self.hashMap[val] = len(self.array)
        self.array.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hashMap:
            return False

        idx = self.hashMap[val]
        last = self.array[-1]

        self.array[idx] = last
        self.array.pop()

        self.hashMap[last] = idx
        del self.hashMap[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.array)

    # Set
    # def __init__(self):
    #     self.array = set()

    # def insert(self, val: int) -> bool:
    #     if val in self.array:
    #         return False
    #     self.array.add(val)
    #     return True

    # def remove(self, val: int) -> bool:
    #     if val in self.array:
    #         self.array.remove(val)
    #         return True
    #     return False

    # def getRandom(self) -> int:
    #     return random.choice(list(self.array))

    # Hash Map
    # def __init__(self):
    #     self.dict = dict()

    # def insert(self, val: int) -> bool:
    #     if self.dict.get(val):
    #         return False
    #     self.dict[val] = True
    #     return True

    # def remove(self, val: int) -> bool:
    #     if self.dict.get(val):
    #         self.dict.pop(val)
    #         return True
    #     return False

    # def getRandom(self) -> int:
    #     return choice(list(self.dict.keys()))
