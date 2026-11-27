class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        for i in nums:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1
        
        n = int((len(nums))/2)
        for key,value in hash_map.items():
            if value > n:
                return key
