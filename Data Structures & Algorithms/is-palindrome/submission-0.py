class Solution:
    def isPalindrome(self, s: str) -> bool:
        word_list = "".join(c.lower() for c in s if c.isalnum())
        word_len = len(word_list)

        for i in range(word_len // 2):
            if word_list[i] != word_list[word_len - i - 1]:
                return False

        return True