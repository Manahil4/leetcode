def romanToInt(s: str) -> int:
    # Mapping Roman numerals to their corresponding values
    roman_to_int = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    # Initialize the total sum
    total = 0
    
    # Iterate through the Roman numeral string
    for i in range(len(s)):
        # If the current value is less than the next value, subtract it
        if i < len(s) - 1 and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
            total -= roman_to_int[s[i]]
        else:
            # Otherwise, add the value
            total += roman_to_int[s[i]]
    
    return total

# Example 1
s1 = "III"
print(romanToInt(s1))  # Output: 3

# Example 2
s2 = "LVIII"
print(romanToInt(s2))  # Output: 58

# Example 3
s3 = "MCMXCIV"
print(romanToInt(s3))  # Output: 1994
      
