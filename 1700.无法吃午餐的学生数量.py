#
# @lc app=leetcode.cn id=1700 lang=python3
#
# [1700] 无法吃午餐的学生数量
#

# @lc code=start
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        for sandwich in sandwiches:
            for i in range(len(students)):
                if students[i] == sandwich:
                    students.pop(i)
                    students = students[i:]+students[:i]
                    break
            else:
                return len(students)
        return 0
# @lc code=end

