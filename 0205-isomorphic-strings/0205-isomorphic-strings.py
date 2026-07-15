class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        map_s = {}
        map_t = {}
        
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            
            if char_s not in map_s:
                map_s[char_s] = i
                
            if char_t not in map_t:
                map_t[char_t] = i

            if map_s[char_s] != map_t[char_t]:
                return False
                
        return True