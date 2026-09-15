class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      # have to check if (1) length is the same, (2) letters are the same, and (3) they exist in the same amount
      if len(s) != len(t):
        return False

      countS, countT = {}, {}

      for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
      return countS == countT