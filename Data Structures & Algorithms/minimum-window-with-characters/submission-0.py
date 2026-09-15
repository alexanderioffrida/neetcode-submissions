class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if t == "":
            return ""
        
        tmap = {}
        window = {}

        for ch in t:
            tmap[ch] = 1 + tmap.get(ch, 0)
        
        have, need = 0, len(tmap)
        res, size = [-1, -1], float("infinity")
        l = 0
        
        for r in range(len(s)):
            ch = s[r]
            window[ch] = 1 + window.get(ch, 0)

            if ch in tmap and window[ch] == tmap[ch]:
                have += 1
            
            while have == need:
                if (r - l + 1) < size:
                    res = [l, r]
                    size = r - l + 1

                window[s[l]] -= 1

                if s[l] in tmap and window[s[l]] < tmap[s[l]]:
                    have -= 1
                
                l += 1
        
        l, r = res

        return s[l : r + 1] if size != float("infinity") else ""


        