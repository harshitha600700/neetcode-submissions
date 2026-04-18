class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph=defaultdict(list)
        #3 conditions:
        #1.connectivity->every node should be connected
        #2.no cycles
        #3.exactly n-1 edges

        if len(edges)!=n-1:
            return False

        #unidirectional
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visit=set()#visit set to store all the nodes that have already been visited to check for cycles

        #dfs with parent helps with false cycle detection
        def dfs(node,parent):
            if node in visit:
                return False
            
            visit.add(node)

            for nei in graph[node]:
                if nei==parent:
                    continue
                if not dfs(nei,node):
                    return False
            return True
        return dfs(0,-1) and len(visit)==n#to ensure no cycle and connectivity



        