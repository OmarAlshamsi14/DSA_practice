class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictt= {}
        for i in nums:
            if i in dictt:
                dictt[i]+=1
            else:
                dictt[i] = 1
        
        sorted_items = sorted(dictt.items(), key=lambda x: x[1], reverse=True)
        result = []        
        for i in range(k):
            result.append(sorted_items[i][0])
        return result