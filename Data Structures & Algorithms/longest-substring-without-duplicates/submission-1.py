class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l , r = 0, 0
        st = set()
        maxilen= 0
        while(r < len(s)):
            
            if s[r] not in st:
                st.add(s[r])
                maxilen = max(maxilen,r-l+1)
                r+=1
            else:
                st.remove(s[l])
                l+=1;
            
            
        return maxilen


        
        