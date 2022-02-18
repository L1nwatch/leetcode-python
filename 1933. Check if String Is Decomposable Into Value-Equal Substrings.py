class Solution:
    def isDecomposable(self, s: str) -> bool:
        length_2_flag = False
        same_char, same_length = s[0], 1
        for i in range(1, len(s)):
            if s[i] == same_char:
                same_length += 1
                if same_length > 3:
                    same_length = 1
            else:
                if same_length == 3:
                    same_char = s[i]
                    same_length = 1
                    continue
                elif same_length == 2 and length_2_flag is False:
                    same_length = 1
                    same_char = s[i]
                    length_2_flag = True
                    continue
                return False
        else:
            if same_length == 3:
                return length_2_flag
            elif same_length == 2 and length_2_flag is True:
                return False
            elif same_length == 2 and length_2_flag is False:
                return True
            else:
                return False
