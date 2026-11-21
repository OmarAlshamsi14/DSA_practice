class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        to_return = []
        dict1 = {}

        for n in range(len(nums)):
            dict1[nums[n]] = n
        
        for z in range(len(nums)):
            diff = target - nums[z]
            if diff in dict1 and dict1[diff] != z:
                to_return.append(z)
                to_return.append(dict1[diff])
                return to_return