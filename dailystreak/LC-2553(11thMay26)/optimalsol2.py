class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            digits = []

            while num > 0:
                digits.append(num % 10)
                num //= 10

            result.extend(digits[::-1])

        return result