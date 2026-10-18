class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] += 1

        for i, n in count.items():
            freq[n].append(i)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res