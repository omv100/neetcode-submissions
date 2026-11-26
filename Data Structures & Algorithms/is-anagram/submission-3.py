class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        containsS = {}
        containsT = {}
        for i in s:
            if i in containsS:
                containsS[i] += 1
            else:
                containsS[i] = 1
        for i in t:
            if i in containsT:
                containsT[i] += 1
            else:
                containsT[i] = 1
        if containsS == containsT:
            return True
        else:
            return False

            
