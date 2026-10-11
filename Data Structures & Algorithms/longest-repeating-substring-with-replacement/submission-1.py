class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
    
        maxi = 0
        # for i in range(len(s)):
        #     mp= {}
        #     maxiFreq = 0
        #     for j in range(i ,len(s)):
                
        #         if s[j] in mp:
        #             mp[s[j]] += 1
                    
        #         else:
        #             mp[s[j]] = 1
        #         maxiFreq = max(maxiFreq,mp[s[j]])
        #         replacement =  j-i+1 - maxiFreq  
        #         if replacement <= k:
        #             maxi = max(maxi,j-i+1)
        #     print(mp)

        mp  = {}
        l = 0
        maxifreq = 0
        for r in range(len(s)):

            if s[r]  in mp:
                mp[s[r]] += 1
            else:
                mp[s[r]] = 1
            maxifreq = max(maxifreq,mp[s[r]])
            remaining = r-l+1 - maxifreq
            while(remaining > k):
                mp[s[l]] -= 1
                l+=1
                remaining = r-l+1 - maxifreq
            if(remaining <= k):
                maxi=max(maxi,r-l+1)
            
        return maxi


                
