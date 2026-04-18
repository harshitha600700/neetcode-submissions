class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visit=set()

        def dfs(node):
            if node in visit:
                return
            
            visit.add(node)
            
            for nei in graph[node]:
                dfs(nei)
        
        components=0
        for i in range(n):
            if i not in visit:
                dfs(i)
                components+=1
        return components
        