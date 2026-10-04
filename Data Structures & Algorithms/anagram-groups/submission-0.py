class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group_dict: dict[str, list[str]] = {}

        for s in strs:
            group_key = ''.join(sorted(s))
            group_dict.setdefault(group_key, []).append(s)

        res: list[list[str]] = []
        for val in group_dict.values():
            res.append(val)

        return res