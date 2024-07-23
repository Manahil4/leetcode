class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""
        
        # Initialize start and end pointers to store the indices of the longest palindromic substring
        start, end = 0, 0
        
        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)       # Odd-length palindromes
            len2 = self.expandAroundCenter(s, i, i + 1)   # Even-length palindromes
            max_len = max(len1, len2)
            
            if max_len > (end - start):
                # Update the start and end pointers
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        return s[start:end + 1]
    
    def expandAroundCenter(self, s, left, right):
        """
        Expand around the center and return the length of the palindrome.
        :type s: str
        :type left: int
        :type right: int
        :rtype: int
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

# Example usage:
solution = Solution()
print(solution.longestPalindrome("babad"))  # Output: "bab" or "aba"
print(solution.longestPalindrome("cbbd"))   # Output: "bb"
