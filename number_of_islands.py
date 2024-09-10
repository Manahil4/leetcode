from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Get the dimensions of the grid
        m, n = len(grid), len(grid[0])

        # Define the DFS function
        def dfs(i, j):
            # Boundary conditions and if it's water or already visited
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            # Mark this cell as visited (change to '0')
            grid[i][j] = '0'
            
            # Call DFS for all 4 directions (right, down, left, up)
            dfs(i, j + 1)  # right
            dfs(i + 1, j)  # down
            dfs(i, j - 1)  # left
            dfs(i - 1, j)  # up

        # Initialize number of islands counter
        num_islands = 0

        # Iterate through the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':  # If we find an unvisited land
                    num_islands += 1    # Increment the island count
                    dfs(i, j)           # Perform DFS to mark the entire island

        return num_islands

# Example Usage:
grid = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]

solution = Solution()
print(solution.numIslands(grid))  # Output: 1
