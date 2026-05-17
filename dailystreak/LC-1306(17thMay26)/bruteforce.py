#time complexity: O(n)
# space complexity: O(n)

#approch create a graph and then do dfs to find the zero value
#then we will mark the visited nodes to avoid cycles and infinite loops
#then we will check if the current node is zero or not if it is zero then we will return true else we will continue to explore the neighbors of the current node

class Solution:
    def canReach(self, arr, start):

        n = len(arr)

        graph = {}

        for i in range(n):

            neighbors = []

            forward = i + arr[i]
            backward = i - arr[i]

            # Valid forward jump
            if forward < n:
                neighbors.append(forward)

            # Valid backward jump
            if backward >= 0:
                neighbors.append(backward)

            graph[i] = neighbors

        visited = set()

        def dfs(node):

            # Already visited
            if node in visited:
                return False
            # Mark visited
            visited.add(node)
            # Found zero
            if arr[node] == 0:
                return True
                
            for neighbor in graph[node]:

                if dfs(neighbor):
                    return True

            return False

        return dfs(start)