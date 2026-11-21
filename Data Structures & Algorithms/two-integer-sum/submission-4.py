class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = 0
        list = []
        for i in range(len(nums)):
            diff = target - nums[i]
            # Copy the array and remove the current element to avoid using same element twice
            temp_nums = nums.copy()
            temp_nums[i] = None  # Mark current position to avoid using it
            
            if diff in temp_nums:
                list.append(i)
                break

        for j in range(len(nums)):
            if nums[j] == diff and j != list[0]:  # Skip if same as first index
                list.append(j)
                break

        return list