class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Sorted function then iterate over list or HashTable + Union Find
        # O(n)

        if not nums:
            return 0
        res = 0
        nums.sort()

        current, cons = nums[0], 0 # current and consecutive streak
        i = 0 # pointer
        while i < len(nums):
            if current != nums[i]:
                current = nums[i]
                cons = 0
            while i < len(nums) and nums[i] == current:
                i += 1
            cons += 1
            current += 1
            res = max(res, cons)
        return res
