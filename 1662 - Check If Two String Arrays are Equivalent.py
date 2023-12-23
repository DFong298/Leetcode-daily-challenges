class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1, i = '', 0
        s2, j = '', 0

        while i < len(word1):
            s1 += word1[i]
            i += 1

        while j < len(word2):
            s2 += word2[j]
            j += 1

        return s1 == s2