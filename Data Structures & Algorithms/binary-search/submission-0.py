class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) -1
        while (lo<=hi):
            length = lo + hi
            mid = (length//2)
            if (nums[mid] > target):
                hi = mid - 1
            elif (nums[mid] == target):
                return mid
            else:
                lo = mid + 1
        return -1