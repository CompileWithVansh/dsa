# Time Complexity: O(n * d)
# Space Complexity: O(n)

# Approach:
# Implicit graph traversal using DFS + memoization
# No extra graph construction
# We try all valid left/right jumps from each index
# dp[i] stores maximum jumps possible starting from i

class Solution:
    def maxJumps(self, arr, d):

        n = len(arr)

        # memoization array
        dp = [-1] * n

        def dfs(index):

            # already calculated
            if dp[index] != -1:
                return dp[index]

            # minimum answer is 1
            # (standing on current index)
            best = 1

            # ---------- RIGHT ----------
            for nextIndex in range(index + 1,
                                   min(n, index + d + 1)):

                # cannot jump to greater/equal
                if arr[nextIndex] >= arr[index]:
                    break

                best = max(best,
                           1 + dfs(nextIndex))

            # ---------- LEFT ----------
            for nextIndex in range(index - 1,
                                   max(-1, index - d - 1),
                                   -1):

                # cannot jump to greater/equal
                if arr[nextIndex] >= arr[index]:
                    break

                best = max(best,
                           1 + dfs(nextIndex))

            dp[index] = best
            return best

        answer = 1

        for i in range(n):
            answer = max(answer, dfs(i))

        return answer