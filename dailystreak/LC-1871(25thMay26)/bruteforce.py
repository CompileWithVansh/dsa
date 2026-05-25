#time complexity: O(n^2)
#space complexity: O(n)


class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        n = len(s)
        visited = set()

        def dfs(i):

            if i == n - 1:
                return True

            visited.add(i)

            for j in range(i + minJump, min(i + maxJump + 1, n)):

                if s[j] == '0' and j not in visited:

                    if dfs(j):
                        return True

            return False

        return dfs(0)