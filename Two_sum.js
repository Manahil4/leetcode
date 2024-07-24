function twoSum(nums, target) {
    // Create a map to store the indices of the elements
    let numMap = new Map();

    // Iterate over the array
    for (let i = 0; i < nums.length; i++) {
        // Calculate the complement
        let complement = target - nums[i];

        // Check if the complement is already in the map
        if (numMap.has(complement)) {
            // If found, return the indices of the complement and the current element
            return [numMap.get(complement), i];
        }

        // Otherwise, add the current element and its index to the map
        numMap.set(nums[i], i);
    }

    // Return an empty array if no solution is found
    return [];
}

// Example usage:
console.log(twoSum([2, 7, 11, 15], 9)); // Output: [0, 1]
console.log(twoSum([3, 2, 4], 6)); // Output: [1, 2]
console.log(twoSum([3, 3], 6)); // Output: [0, 1]
      
