from collections import deque

class LRUCache:
    """
    Least recently used in cache
    get
      - if key in cache update the key to the most recently cached and return value
      - else return -1
    
    put
      - if key in cache, update the value and the key to the most recently cached
      - else
        - if cahce is full, **remove the oldest cache**
        - cache k, v and update k as the most recently cached
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru = deque()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.lru.remove(key)
            self.lru.appendleft(key)
            return self.cache.get(key)

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.lru.remove(key)
            self.lru.appendleft(key)
        else:
            if len(self.cache) == self.capacity:
                oldest_key = self.lru.pop()
                del self.cache[oldest_key]
            self.cache[key] = value
            self.lru.appendleft(key)