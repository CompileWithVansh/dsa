# Approach:
# 1. Build prefix maximum array.
# 2. Traverse from right to left while maintaining suffix minimum.
# 3. If pre_max[i] > suf_min:
#        ans[i] = ans[i+1]
#    else:
#        ans[i] = pre_max[i]

# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        ans = [0] * n

        # prefix maximum
        pre_max = [0] * n
        pre_max[0] = nums[0]

        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], nums[i])

        suf_min = float('inf')

        # traverse from right to left
        for i in range(n - 1, -1, -1):

            if pre_max[i] > suf_min:

                # connected with right side
                if i + 1 < n:
                    ans[i] = ans[i + 1]
                else:
                    ans[i] = pre_max[i]

            else:
                ans[i] = pre_max[i]

            suf_min = min(suf_min, nums[i])

        return ans
        