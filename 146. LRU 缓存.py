class LRUCache:

    def __init__(self, capacity: int):
        self.data = dict()
        self.lru = list()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.data:
            index = self.lru.index(key)
            self.lru.pop(index)
            self.lru.append(key)
            return self.data[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.data:
            if len(self.lru) == self.capacity:
                old = self.lru.pop(0)
                del self.data[old]
            self.data[key] = value
            self.lru.append(key)
        else:
            self.data[key] = value
            self.get(key)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)