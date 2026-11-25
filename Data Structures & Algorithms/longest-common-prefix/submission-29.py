class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        minimum_len = len(strs[0])
        minidx = 0

        for i in range(len(strs)):
            if len(strs[i]) < minimum_len:
                minimum_len = len(strs[i])
                minidx = i

        reference = strs[minidx]

        for index in range(minimum_len):
            for s in strs:
                if s[index] != reference[index]:
                    return reference[:index]

        return reference