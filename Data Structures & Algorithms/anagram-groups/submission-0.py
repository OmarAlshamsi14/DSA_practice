class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Dict = defaultdict(list)
        for s in strs:
            sortedS = "".join(sorted(s))
            Dict[sortedS].append(s)
        return Dict.values()