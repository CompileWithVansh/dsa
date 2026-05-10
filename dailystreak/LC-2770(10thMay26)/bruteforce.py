#TIME COMPLEXITY: O(N^N)
#SPACE COMPLEXITY: O(N)
#BRUTE FORCE SOLUTION
#gives tle so dont use 


class Solution:
    def maximumJumps(self, nums, target):
        n = len(nums)

        def dfs(i):
            # reached last index
            if i == n - 1:
                return 0

            max_jumps = -float('inf')

            # try every possible next jump
            for j in range(i + 1, n):

                if -target <= nums[j] - nums[i] <= target:

                    result = dfs(j)

                    if result != -float('inf'):
                        max_jumps = max(max_jumps, 1 + result)

            return max_jumps

        ans = dfs(0)

        return ans if ans != -float('inf') else -1