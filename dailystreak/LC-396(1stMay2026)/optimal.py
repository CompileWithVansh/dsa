

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        
        n = len(nums)
        s = 0
        for i in nums:
            s += i

        b = 0
        for i in range(n):
            b += i * nums[i]
        maxx = b

        for i in range(n - 1, 0, -1):
            b = b + s - (n * nums[i])

            if b > maxx:
                maxx = b

        return maxx