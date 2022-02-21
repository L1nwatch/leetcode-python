class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length_s1, length_s2 = len(s1), len(s2)
        if length_s1 > length_s2:
            return False

        from collections import Counter
        count_s1 = Counter(s1)
        count_s2 = Counter(s2[:length_s1])
        if count_s1 == count_s2:
            return True
        
        for i in range(length_s1,length_s2):
            new_char,old_char = s2[i], s2[i-length_s1]
            count_s2[new_char] = count_s2.get(new_char,0) + 1
            count_s2[old_char] -= 1
            if count_s1 == count_s2:
                return True
        return False
