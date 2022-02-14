class TwoSum:

    def __init__(self):
        self.nums = list()
        self.sum = set()


    def add(self, number: int) -> None:
        for num in self.nums:
            self.sum.add(num+number)
        self.nums.append(number)

    def find(self, value: int) -> bool:
        return value in self.sum




# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)