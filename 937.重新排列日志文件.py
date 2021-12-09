#
# @lc app=leetcode.cn id=937 lang=python3
#
# [937] 重新排列日志文件
#

# @lc code=start
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        alpha_list, alnum_list = list(), list()
        count = 0
        for log in logs:
            if str(log[log.find(" "):]).replace(" ", "").isdigit():
                alnum_list.append(log)
            else:
                index = 0
                while index < count:
                    first_space = alpha_list[index].find(" ")
                    flag, content = alpha_list[index][:first_space], alpha_list[index][first_space:]

                    first_space = log.find(" ")
                    cur_flag, cur_content = log[:first_space], log[first_space:]

                    if cur_content < content:
                        break
                    elif cur_content == content:
                        if cur_flag < flag:
                            break
                        else:
                            index += 1
                    else:
                        index += 1
                alpha_list.insert(index, log)
                count += 1

        alpha_list.extend(alnum_list)
        return alpha_list

# @lc code=end
