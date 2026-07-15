class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        t = {}
        f = {}
        sp = s.split(" ")
        if len(pattern) != len(sp):
            return False
        for i in range(len(pattern)):
            char = pattern[i]
            word =  sp[i]
            if (char in t and t[char] != word):
                return False
            if (word in f and f[word] != char):
                return False
            t[char] = word
            f[word] = char

        return True