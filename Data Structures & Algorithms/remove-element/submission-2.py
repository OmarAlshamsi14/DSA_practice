class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        old_length = len(nums)
        k = 0

        for i in range(old_length):
            if nums[i] == val:
                nums[i] = 999999999999999999
                k+=1
        nums.sort()
        
        new_length = old_length - k
        return new_length
