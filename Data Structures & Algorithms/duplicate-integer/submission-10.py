class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        SET = set(nums)
        length = len(nums)
        if len(SET) < length:
            return True
        else:
            return False  