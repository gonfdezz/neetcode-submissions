class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        listForS = sorted(list(s))
        listForT = sorted(list(t))
        if listForS == listForT:
            return True
        return False
