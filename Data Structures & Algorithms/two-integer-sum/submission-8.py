class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_array = []
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if (nums[i] + nums[j+1] == target) and i!=(j+1):
                    index_array.append(i)
                    index_array.append(j+1)
                    return index_array
        
