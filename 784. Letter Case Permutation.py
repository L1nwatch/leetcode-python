#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" Description
"""

__author__ = '__L1n__w@tch'

class Solution2:
    """
    TLE
    """
    def dfs(self,first=0):
        self.answer.append(self.s[:])
        for i in range(first,self.length):
            if not self.s[i].isdigit():
                temp = self.s[i]
                self.s[i] = self.s[i].lower() if self.s[i].isupper() else self.s[i].upper()
                self.dfs(first+1)
                self.s[i] = temp


    def letterCasePermutation(self, s: str) -> List[str]:
        self.answer = list()
        self.length = len(s)
        self.s = list(s)
        self.dfs()
        return ["".join(x) for x in self.answer]

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        answer = [[]]
        length = len(s)

        for char in s:
            length = len(answer)
            if char.isalpha():
                for i in range(length):
                    answer.append(answer[i][:])
                    answer[i].append(char.lower())
                    answer[length+i].append(char.upper())
            else:
                for i in range(length):
                    answer[i].append(char)

        return ["".join(x) for x in answer]

class Solution3:
    def letterCasePermutation(self, s: str) -> List[str]:
        answer = [[]]
        for char in s:
            if not char.isdigit():
                for j in range(len(answer)):
                    answer.append(answer[j][:])
                    answer[-1].append(char.upper())
                    answer[j].append(char.lower())
            else:
                for i in range(len(answer)):
                    answer[i].append(char)
        return ["".join(x) for x in answer]
        