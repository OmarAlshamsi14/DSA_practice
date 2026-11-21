class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        b = sorted(s)
        c = sorted (t)
        return c == b
