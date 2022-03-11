#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" Description
"""

__author__ = '__L1n__w@tch'

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        return list(permutations(nums))


class Solution2:
    def dfs(self,first=0):
        if first == self.length:
            self.answer.append(self.nums[:])
        for i in range(first,self.length):
            self.nums[i],self.nums[first] = self.nums[first],self.nums[i]
            self.dfs(first+1)
            self.nums[i],self.nums[first] = self.nums[first],self.nums[i]

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.answer = list()
        self.length = len(nums)
        self.dfs()
        return self.answer

class Solution3:
    def dfs(self,first=0):
        if first == self.length:
            self.answer.append(self.nums[:])
        for i in range(first,self.length):
            self.nums[i],self.nums[first] = self.nums[first],self.nums[i]
            self.dfs(first+1)
            self.nums[i],self.nums[first] = self.nums[first],self.nums[i]

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.answer = list()
        self.nums = nums
        self.length = len(nums)
        self.dfs()
        return self.answer