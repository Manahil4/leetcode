class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        str_x=str(x)
        return str_x==str_x[::-1]
# Conversion to String: str_x = str(x) converts the integer x to its string representation.
# Reversal of String: str_x[::-1] creates a new string that is the reverse of str_x. The slice notation [::-1] means:
# : indicates the full range of the string.
# The first : means to include all characters.
# The second : followed by -1 indicates the step, i.e., traverse the string from end to start.
