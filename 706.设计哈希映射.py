#
# @lc app=leetcode.cn id=706 lang=python3
#
# [706] 设计哈希映射
#

# @lc code=start
class MyHashMap:

    def __init__(self):
        self.dict = dict()

    def put(self, key: int, value: int) -> None:
        self.dict.update({key: value})

    def get(self, key: int) -> int:
        return self.dict.get(key, -1)

    def remove(self, key: int) -> None:
        if key in self.dict:
            del self.dict[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end
