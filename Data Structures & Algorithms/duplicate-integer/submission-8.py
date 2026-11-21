class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c= set()
        for i in nums:
            if i not in c:
                c.add(i)
            else:
                return True
        return False
    