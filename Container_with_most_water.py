def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0
    
    while left < right:
        # Calculate the width and the height of the container
        width = right - left
        height_left = height[left]
        height_right = height[right]
        current_area = min(height_left, height_right) * width
        
        # Update the maximum area found
        max_area = max(max_area, current_area)
        
        # Move the pointer pointing to the shorter line
        if height_left < height_right:
            left += 1
        else:
            right -= 1
            
    return max_area
