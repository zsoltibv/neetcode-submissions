class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded = []

        for n in strs:
            str_len = str(len(n))   
            encoded.append(str_len + "#" + n)

        return "".join(encoded)

    def decode(self, s: str) -> list[str]:
        decoded = []

        i = 0
        while i < len(s):

            word_len = ""
            while s[i] >= '0' and s[i] <= '9':
                word_len += s[i]
                i += 1

            i-=1    
            word_len = int(word_len)

            decoded.append(s[i+2:i+2+word_len])
            i = i + 2 + word_len

        return decoded