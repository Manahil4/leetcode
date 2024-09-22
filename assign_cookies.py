class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        child=0
        cooky=0
        while child < len(g) and cooky < len(s) :
            if  s[cooky] >= g[child]:
                child += 1
            cooky += 1
        return child   
