class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        edges = [[] for _ in range(numCourses)] # adjacency list
        in_degree = [0]*numCourses # number of prerequisites for each course
        stack = []
        
        for course, prereq in prerequisites:
            edges[prereq].append(course)
            in_degree[course]+=1
            
        for i in range(numCourses):
            if in_degree[i]==0:     # no prerequisite, can just complete
                stack.append(i)
                
        cnt = 0
        
        while stack:
            p = stack.pop()
            cnt += 1
            for to in edges[p]:
                in_degree[to] -= 1  # complete this prerequisite
                if in_degree[to] == 0:
                    stack.append(to)
                    
        return cnt == numCourses    # number of courses we can complete 
        