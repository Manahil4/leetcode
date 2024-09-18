from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses, prerequisites):
        # Step 1: Create the adjacency list representation of the graph
        adj_list = defaultdict(list)
        indegree = [0] * numCourses

        # Step 2: Populate the adjacency list and indegree array
        for dest, src in prerequisites:
            adj_list[src].append(dest)  # Edge from src -> dest
            indegree[dest] += 1         # Increment indegree for the destination course

        # Step 3: Initialize the queue with all courses having no prerequisites (indegree = 0)
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        # Step 4: Initialize the counter for visited courses
        visited_courses = 0

        # Step 5: Process the queue using BFS
        while queue:
            current_course = queue.popleft()
            visited_courses += 1

            # For each neighbor of the current course, reduce their indegree by 1
            for neighbor in adj_list[current_course]:
                indegree[neighbor] -= 1

                # If indegree becomes 0, add it to the queue
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 6: If the number of visited courses equals the total number of courses, return True
        return visited_courses == numCourses

# Example Usage:
numCourses = 4
prerequisites = [[1, 0], [2, 1], [3, 2]]
solution = Solution()
print(solution.canFinish(numCourses, prerequisites))  # Output: True
# for course shedule code
# algo;
# make a dictionary o r ahash map for storing eah course with value of prerequisites course , from given input  [[0,1],[1,3],[3,4],[0,2]] here 0 is dependent on all courses and overall all courses can be taken . courses as given in list on left are place as key(course name) while on right side are as value(pre requisite of that course) . then use dfs approach , iterate through dictionary , see course and put it in VisitSet( a set initialize for storing visit courses) and then see its prerequisite( now consider it as course and repeat above process means put it in visitset and search it pre requisite this repeats till if any course have no any  prerequisite so returning back to course that depend on that prereuisite you see we iterate in dfs approach means go down till leaf node but now after  returning back check for any other sucessor means any other prerequisite then repeat above process )  
