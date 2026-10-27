class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        duplicate_set = set()
        l = 0
        max_length = 0

        for r in range(len(s)):
            while s[r] in duplicate_set:
                duplicate_set.remove(s[l])
                l += 1

            duplicate_set.add(s[r])
            max_length = max(max_length, r - l + 1)

        return max_length