from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charFreq: dict[str, int] = defaultdict(int)
        l = 0
        maxLength = 0

        for r in range(len(s)):
            charFreq[s[r]] += 1

            while (r - l + 1) - max(charFreq.values()) > k:
                charFreq[s[l]] -= 1
                l += 1

            maxLength = max(maxLength, r - l + 1) 

        return maxLength