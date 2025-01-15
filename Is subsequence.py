class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        k = len(t)
        if len(s) == 0:
            return True
        while j < k:
            if i == len(s) and i > j:
                return False
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
            if i == len(s):
                return True
        return False