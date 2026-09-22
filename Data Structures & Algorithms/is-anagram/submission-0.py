class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1=[0]*26
        c2=[0]*26
        for y in s:
            c1[ord(y)-ord('a')]=c1[ord(y)-ord('a')]+1
        for u in t:
            c2[ord(u)-ord('a')]=c2[ord(u)-ord('a')]+1


        for i in range(0,len(c1)):
            if c1[i]!=c2[i]:
                return False
                break
        return True        
            
                    

        