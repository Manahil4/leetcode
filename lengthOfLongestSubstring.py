class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub_lengths = []
        sub = ''

        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[j] in sub:
                    sub_lengths.append(len(sub))
                    sub = ''
                    continue 
                sub += s[j]

            sub_lengths.append(len(sub))
            sub = ''

        return max(sub_lengths) if sub_lengths else 0
