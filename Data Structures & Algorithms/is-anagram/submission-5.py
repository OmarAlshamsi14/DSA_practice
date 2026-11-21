class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(t) != len(s):
            return False
        
        dict1 = {}
        dict2 = {}

        for n in s:
            if n in dict1:
                dict1[n]+=1
            else:
                dict1[n] = 1
            
        for z in t:
            if z in dict2:
                dict2[z]+=1
            else:
                dict2[z] = 1

        return dict1 == dict2   