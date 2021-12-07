#
# @lc app=leetcode.cn id=929 lang=python3
#
# [929] 独特的电子邮件地址
#

# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        answer = set()
        for email in emails:
            address, domain = email.split("@")
            actual_address = str()
            for char in address:
                if char == ".":
                    continue
                elif char == "+":
                    break
                else:
                    actual_address += char
            answer.add(f"{actual_address}@{domain}")

        return len(answer)
# @lc code=end
