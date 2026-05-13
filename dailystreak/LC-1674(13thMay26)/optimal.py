#time complexity: O(n + m) where n is the length of nums and m is the range of possible sums (2*limit)
#space complexity: O(m) where m is the range of possible sums (2*limit


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)

        # Initially every pair costs 2 moves
        pairs = n // 2

        for i in range(pairs):
            a = nums[i]
            b = nums[n - 1 - i]

            low = min(a, b) + 1
            high = max(a, b) + limit
            s = a + b

            # one move range
            diff[low] -= 1
            diff[high + 1] += 1

            # exact sum -> one more reduction
            diff[s] -= 1
            diff[s + 1] += 1

        ans = float('inf')
        curr = pairs * 2

        for target in range(2, 2 * limit + 1):
            curr += diff[target]
            ans = min(ans, curr)

        return ans