class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)

        if len(s) != len(t):
            return False

        for char_s, char_t in zip(s, t):
            if char_s != char_t:
                return False

        return True