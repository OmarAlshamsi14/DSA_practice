class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        to_return = []
        dict1 = {}

        for n in range(len(nums)):
            dict1[nums[n]] = n
        
        for i in range(len(nums)):
            j = target - nums[i]
            if j in dict1 and dict1[j] != i:
                to_return.append(i)
                to_return.append(dict1[j])
                return to_return