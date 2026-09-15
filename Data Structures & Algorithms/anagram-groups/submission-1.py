class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a hashmap of k: ltrcount, v: number | iterate over shared numbers
        solution = defaultdict(list)

        for s in strs:
            solution[tuple(sorted(s))].append(s)
        return list(solution.values())