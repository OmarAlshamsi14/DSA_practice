class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.upper()
        new = ""
        for i in s:
            if i.isalpha() != True and i.isdigit()  != True :
                continue
            else:
                new +=i
    
        opposite = new[::-1]

        return (new == opposite)