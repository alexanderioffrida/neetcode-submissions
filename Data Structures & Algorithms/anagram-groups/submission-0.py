class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a hashmap of k: ltrcount, v: number | iterate over shared numbers
        solution = defaultdict(list)

        for s in strs:
          count = [0] * 26 # a ... z where each charCount starts @ 0

          for c in s: # iterate through all characters in the string
            count[ord(c) - ord("a")] += 1 # extract and compare ascii values

          solution[tuple(count)].append(s) # count is a list, but in python, a list cannot be keys –– needs to be a tuple

        return list(solution.values()) # just returning the values –– anagrams grouped together