class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = int(len(nums)/2)
        for i in range(len(nums)):
            if nums[i] == nums[i+n]:
                return nums[i]

        