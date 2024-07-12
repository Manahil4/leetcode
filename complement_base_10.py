# The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

# For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
# Given an integer n, return its complement

# _________________________________________Q solution______________________________________#
class Solution(object):
    def bitwiseComplement(self, n):
        # Calculate the bitwise complement of n by flipping all its bits
        not_of_n = ~n  # Inverts all the bits of n

        # Initialize m to hold a copy of n
        m = n
        
        # Initialize the mask with all bits set to 0
        mask = 0
        
        # If n is 0, the bitwise complement will be 1 (special case)
        if n == 0:
            mask = (mask << 1) | 1  # Set the rightmost bit of the mask to 1
        
        else:
            # Find the appropriate mask length
            while n != 0:
                mask = (mask << 1) | 1  # Shifts mask one position to the left and sets the rightmost bit to 1
                n = n >> 1             # Shifts n one position to the right
        
        # Perform bitwise AND operation between the mask and the bitwise complement of n
        ans = mask & not_of_n  # Retains only the bits where both mask and not_of_n have a 1

        return ans

a = Solution()
output = a.bitwiseComplement(5)
print(output)  # Output will be 2, which is the bitwise complement of 5 (101), resulting in 010
