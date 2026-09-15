class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        S = []
        for i, num in enumerate(nums):
          S.append([num, i])

        S.sort()
        i, j = 0, len(nums) - 1
        while i < j:
          test = S[i][0] + S[j][0]
          if test == target:
            return [min(S[i][1], S[j][1]),
                    max(S[i][1], S[j][1])]
          elif test < target:
            i += 1
          else:
            j -= 1
        return []

