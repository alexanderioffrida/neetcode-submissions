class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zc = 1, 0
        for num in nums:
            if num:
                prod *= num
            else:
                zc += 1
        if zc > 1: return [0] * len(nums)

        sol = [0] * len(nums)
        for i, c in enumerate(nums):
            if zc: sol[i] = 0 if c else prod
            else: sol[i] = prod // c
        return sol