#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" Description
"""

__author__ = '__L1n__w@tch'


class Solution:
    def dfs(self,first=0):
        if first == self.length:
            self.answer.append(self.nums[:])
        for i in range(first, self.length):
            self.nums[i], self.nums[first] = self.nums[first], self.nums[i]
            self.dfs(first+1)
            self.nums[i], self.nums[first] = self.nums[first], self.nums[i]

    def permute(self, nums: list[int]) -> list[list[int]]:
        self.answer = list()
        self.nums = nums
        self.length = len(nums)
        self.dfs(0)
        return self.answer


if __name__ == "__main__":
    pass
