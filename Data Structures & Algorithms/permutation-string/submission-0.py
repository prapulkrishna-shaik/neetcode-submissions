class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        for i in range(len(s2)):
            dummy = ""
            for j in range(i,len(s2)):
                dummy += s2[j]
                if len(dummy) == len(s1):
                    if sorted(s1) == sorted(dummy):
                        return True
                    break
        return False
        