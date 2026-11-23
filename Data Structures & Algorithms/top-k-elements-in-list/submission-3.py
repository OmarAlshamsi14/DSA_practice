class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash_map = {}
        k_most = []

        for i in nums:
            if i in hash_map:
                hash_map[i] +=1
            else:
                hash_map[i] = 1
        
        sorted_pairs = sorted(hash_map.items(), key=lambda pair: pair[1], reverse=True)
        
        to_return = []
        for i in range(k):
            to_return.append(sorted_pairs[i][0])

        return to_return
