class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # HashMap KV Pairs: number and count | return k most frequent
        count = {}
        for num in nums:
          count[num] = 1 + count.get(num, 0)

        freq = [[] for _ in range(len(nums) + 1)]
        for num, c in count.items():
            freq[c].append(num)

        sol = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                sol.append(num)
                if len(sol) == k:
                    return sol

        