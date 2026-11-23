class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sorted_list = []
        for i in strs:
            sorted_list.append(''.join(sorted(i)))

        hash_map = {}
        
        for s in range(len(sorted_list)):
            if sorted_list[s] not in hash_map:
                hash_map[sorted_list[s]] = [s]
            else:
                hash_map[sorted_list[s]].append(s)
        sublists = []
        
        for key, value in hash_map.items():
            sub = []
            for j in value:
                sub.append(strs[j])
                
            sublists.append(sub)
        return sublists