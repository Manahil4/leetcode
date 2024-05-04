# The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

# For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
# Given an integer n, return its complement

# _________________________________________Q solution______________________________________#


# reverse int bit and return corresponding int value against that bits 
# Not operator :not all bits in given int eg101->010 but every no is 32 or 64 bit longer for int 5 in binary is 29 0's and then 101 if i not it i get 29 1's ans then 010 which is 2 but i don't want these starting 1s 
# i can and the 'not value' with the union of input integer value with its not version so i get 29 0's at the start and 010 at last 3 bits so automatically it will translate into int 2

# class Solution(object):
#     def complement_int_of_base10(self, n):
#         not_of_n=~n#29 bits containing 1's,then 010
#         mask=n | not_of_n#29 bits containing 0's and 101 OR 29 bits containing 1's and 010 . result in 29 bits containing 1's and 111.(means all 1s)
#         ans=mask & not_of_n#all ones and 29 1's and 010->29 0s and 010
#         return ans
# a=Solution()  
# output=a.complement_int_of_base10(5)
# print(output)
# # 101->
# # 110->11111111010
class Solution(object):
    def bitwiseComplement(self, n):
        if n == 0:
            return 1  # Special case: complement of 0 is 1
        
        num = 0
        i = 0

        while n != 0:
            bit = n & 1              # Extracting the least significant bit
            rev = bit ^ 1            # Computing the complement of the extracted bit
            n = n >> 1               # Right shifting n to get the next bit

            if rev == 1:
                num += 2 ** i * rev  # Adding the complemented bit to the result

            i += 1                   # Incrementing the position counter

        return num                  # Returning the complemented number

# Test
a = Solution()  
output = a.bitwiseComplement(0)
print(output)  # Output: 1

