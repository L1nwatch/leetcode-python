class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotate_num_map = {
            "0":"0",
            "1":"1",
            "6":"9",
            "8":"8",
            "9":"6"
        }

        length = len(num)
        for i in range(length//2+1):
            if num[i] in rotate_num_map:
                if num[length-i-1] != rotate_num_map[num[i]]:
                    return False
            else:
                return False
        return True