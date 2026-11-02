from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        charFreqS1 = defaultdict(int)
        charFreqS2 = defaultdict(int)
        lenS1 = len(s1)
        lenS2 = len(s2)
    
        if lenS1 > lenS2:
            return False

        for i in range(lenS1):
            charFreqS1[s1[i]] += 1

        l = 0 
        for r in range(lenS2):
            charFreqS2[s2[r]] += 1

            if r - l + 1 > lenS1:
                charFreqS2[s2[l]] -= 1
                l += 1

            if r - l + 1 == lenS1:
                ok = True
                for ch, freq in charFreqS1.items():
                    if charFreqS2[ch] != freq:
                        ok = False
                        break

                if ok == True:
                    return True

        return False