class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        sizes, sol = [], ""

        for s in strs:
            sizes.append(len(s))
        
        for size in sizes:
            sol += str(size)
            sol += ','
        sol += '@'

        for s in strs:
            sol += s
        return sol

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        sizes, sol, i = [], [], 0

        while s[i] != '@':
            crnt = ""
            while s[i] != ',':
                crnt += s[i]
                i += 1
            sizes.append(int(crnt))
            i += 1
        i += 1
        for size in sizes:
            sol.append(s[i:i + size])
            i += size
        return sol
