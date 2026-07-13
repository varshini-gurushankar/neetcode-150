class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        map1 = {}
        map2 = {}

        for n in s:
            map1[n] = 1 + map1.get(n, 0)

        for n in t:
            map2[n] = 1 + map2.get(n, 0) 

        return map1 == map2

        

