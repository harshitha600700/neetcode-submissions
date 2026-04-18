#this prgram is for bascially checking whether theres a cycle in the graph or not
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph=defaultdict(list)#each curse->list of courses dependent on it 
        for a,b in prerequisites:#[a,b] and a dependednt on b 
            graph[b].append(a)
        
        #each course has 3 states:
        #0->not visited
        #1->currently visiting
        #2->already visited

        visit=[0]*numCourses

        def dfs(node):
            if visit[node]==1:
                return False
            if visit[node]==2:
                return True
            visit[node]=1

            #go thru all the dependent courses
            for nei in graph[node]:
                if not dfs(nei):
                    return False

            visit[node]=2
            return True
            
            #disconnected graphs
            
        for nei in range(numCourses):
            if not dfs(nei):
                return False
        return True