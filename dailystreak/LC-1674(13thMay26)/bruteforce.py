#gives tle dont try
##time complexity: O(n * m) where n is the length of nums
# and m is the range of possible sums (2*limit)  
#space complexity: O(1) as we are using constant space


class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        ans = float('inf')

        for target in range(2, 2 * limit + 1):

            moves = 0


            for i in range(n // 2):

                a = nums[i]
                b = nums[n - 1 - i]

                # 0 move
                if a + b == target:
                    continue

                # 1 move possible
                elif (1 <= target - a <= limit or
                      1 <= target - b <= limit):

                    moves += 1

                # otherwise 2 moves
                else:
                    moves += 2

            ans = min(ans, moves)

        return ans
         