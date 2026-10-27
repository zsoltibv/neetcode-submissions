class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        duplicateSet = set()
        l = 0
        max_length = 0

        for r in range(len(s)):
            while s[r] in duplicateSet:
                duplicateSet.remove(s[l])
                l += 1

            duplicateSet.add(s[r])
            max_length = max(max_length, r - l + 1)

        return max_length