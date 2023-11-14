class Solution:
    def sortVowels(self, s: str) -> str:
        v_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E','I', 'O', 'U'}
        vowels = []
        t = []
        for c in s:
            if c in v_set:
                t.append('.')
                vowels.append(c)
            else:
                t += c

        vowels.sort(reverse=True)
        for i in range(len(t)):
            if t[i] == '.':
                t[i] = vowels.pop()

        return ''.join(t)
        