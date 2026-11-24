class Solution:
    def isPalindrome(self, s: str) -> bool:
     #   s = ''.join(ch.lower() for ch in s if ch.alnum())
        #simplified version of this 
        new_s = ''
        for ch in s:
            if ch.isalnum():
                new_s += ch.lower()
        l,r = 0,len(new_s)-1
        while l<r:
            if new_s[l] != new_s[r]:
                return False
            l += 1
            r -= 1
        return True
        
