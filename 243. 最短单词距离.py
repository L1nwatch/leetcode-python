class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        length = len(wordsDict)
        answer = length
        w1_index, w2_index = None, None
        for i in range(length):
            if wordsDict[i] == word1:
                w1_index = i
            elif wordsDict[i] == word2:
                w2_index = i
            if w1_index is not None and w2_index is not None:
                answer = min(abs(w2_index-w1_index),answer)
        return answer