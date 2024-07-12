class Solution(object):
    def hammingWeight(self, n):
        """
        Function to calculate the Hamming weight (number of set bits) of a positive integer.
        
        :type n: int
        :rtype: int
        """
        # Initialize count to store the number of set bits
        count = 0
        
        # Iterate through each bit of the input number until it becomes 0
        while n:
            # Check if the least significant bit of n is 1 using bitwise AND operation
            if n & 1:
                # Increment count if the least significant bit is 1
                count += 1
            
            # Right shift n by 1 bit to examine the next bit
            n >>= 1
        
        # Return the count of set bits
        return count

# Test cases
a = Solution()

print(a.hammingWeight(11))           # Output: 3
print(a.hammingWeight(128))          # Output: 1
print(a.hammingWeight(2147483645))   # Output: 30
