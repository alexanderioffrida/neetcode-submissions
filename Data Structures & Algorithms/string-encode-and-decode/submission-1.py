class Solution:

    def encode(self, strs: List[str]) -> str:
        sol = ""

        for s in strs:
            sol += str(len(s)) + "@" + s
        return sol

    def decode(self, s: str) -> List[str]:      
        sol, i = [], 0

        while i < len(s):
            j = i
            while s[j] != '@':
                j += 1
            length = int (s[i:j])
            i = j + 1
            j = i + length
            sol.append(s[i:j])
            i = j

        return sol
