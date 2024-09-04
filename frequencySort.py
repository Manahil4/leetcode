from collections import Counter

class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Correcting the typo and importing Counter
        count = Counter(nums)
        
        # Custom sort function
        def custom_sort(n):
            return (count[n], -n)
        
        # Sorting the nums list using custom sort logic
        nums.sort(key=custom_sort)
        return nums
