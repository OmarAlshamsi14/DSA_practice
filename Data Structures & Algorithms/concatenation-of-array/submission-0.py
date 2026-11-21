class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        arr2 = nums.copy()
        full_array = nums + arr2
        return full_array