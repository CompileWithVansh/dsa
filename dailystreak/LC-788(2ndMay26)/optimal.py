class Solution:
    def rotatedDigits(self, n: int) -> int:
        """
        its just a cleaner version
        TC: O(n * log n) - iterate through n numbers, and for each number check digits (log n operations)
        SC: O(1) - only using constant extra space for variables
        """
        
        count = 0

        for num in range(1, n + 1):

            temp = num
            valid = True
            changed = False

            while temp > 0:

                digit = temp % 10

                if digit in [3, 4, 7]:
                    valid = False
                    break

                if digit in [2, 5, 6, 9]:
                    changed = True

                temp //= 10

            if valid and changed:
                count += 1

        return count