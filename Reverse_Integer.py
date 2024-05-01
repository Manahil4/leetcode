class Solution(object):
    def reverse(self, x):
        # Define the maximum and minimum limits for a 32-bit signed integer
        Max = (2 ** 31) - 1
        Min = (-2 ** 31)
        ans = 0  # Initialize the variable to store the reversed integer
        
        # Loop until the input integer becomes zero
        while x != 0:
            digit = abs(x) % 10  # Extract the last digit of the input integer
            # Check if multiplying the current answer by 10 and adding the last digit will cause overflow
            if (x > (Max // 10)) or (x < (Min // 10)):
                return 0  # If overflow is detected, return 0
                
            ans = (ans * 10) + digit  # Add the last digit to the answer after shifting it left by one position
            x = x // 10  # Remove the last digit from the input integer using integer division
        if x < 0:
            return -ans
        else:
            return ans  # Return the reversed integer
