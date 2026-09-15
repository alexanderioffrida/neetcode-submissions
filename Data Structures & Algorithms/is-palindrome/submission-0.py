class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = "".join(ch.lower() for ch in s if ch.isalnum())
        
        l = 0
        r = len(clean_s) - 1

        while l < r:
            if clean_s[l] != clean_s[r]:
                return False
            l += 1;
            r -= 1;
        
        return True
                    
