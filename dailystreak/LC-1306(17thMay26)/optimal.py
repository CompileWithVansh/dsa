#time complexity: O(n)
#space complexity: O(n)
#approch graph implicit traversal using dfs
#NO EXTRA SPACE FOR GRAPH CONSTRUCTION 
#SPACE COMPLEXITY IS O(N) DUE TO RECURSION STACK AND VISITED ARRAY BUT BETTER 
#THAN THE BRUTE FORCE APPROACH WHICH ALSO USES O(N) SPACE FOR GRAPH CONSTRUCTION

class Solution:
    def canReach(self, arr, start):

        visited = [False] * len(arr)

        def dfs(index):

            # Out of bounds
            if index < 0 or index >= len(arr):
                return False

            # Already visited
            if visited[index]:
                return False

            # Found 0
            if arr[index] == 0:
                return True

            # Mark visited
            visited[index] = True

            # Move forward
            forward = index + arr[index]

            # Move backward
            backward = index - arr[index]

            return dfs(forward) or dfs(backward)

        return dfs(start)