class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # HashMap KV Pairs: number and count | return k most frequent
        count = {}
        for num in nums:
          count[num] = 1 + count.get(num, 0)

        arr = []
        for num, c in count.items(): # this gives us key-value pairs
          arr.append([c, num]) # we're gonna add the count and number to the list
        arr.sort() # sort the list by count

        sol = []
        while len(sol) < k:
          sol.append(arr.pop()[1])
        return sol

        