# Week6_due_Sat_November_11
# Question 1
# Minimum add to make parentheses valid (Medium)


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        
        # Build the graph
        for course, prereq in prerequisites:
            graph[prereq].append(course)
        
        # Visit each course
        for course in range(numCourses):
            if not self.dfs(course, graph, visited):
                return False
        
        return True

    def dfs(self, course, graph, visited):
        # If it's already visited, no need to do anything
        if visited[course] == -1:
            return True
        # If it's in the process of visiting, then we've found a cycle
        if visited[course] == 1:
            return False

        # Mark as visiting
        visited[course] = 1
        for neighbor in graph[course]:
            if not self.dfs(neighbor, graph, visited):
                return False
        
        # Mark as visited
        visited[course] = -1
        return True
