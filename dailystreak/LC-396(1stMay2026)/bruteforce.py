
# CODE does not run because of the TLE, but the logic is correct. 
# Time: O(n^2), Space: O(n)
#1st try

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        f=[]
        a=[]
        temp=nums.copy()

        for i in range(0,len(nums)):
            a.append(i)

        for i in range(0,len(nums)):
            b= [x * y for x, y in zip(temp, a)]
            c=sum(b)
            f.append(c)
            a= a[1:] + a[:1]

        return(max(f))
    
# Time: O(n^2), Space: O(n)
#2nd try(cleaner version)
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:

        maximum=float('-inf')
        a = list(range(len(nums)))

        for i in range(0,len(nums)):
            b=sum(x * y for x, y in zip(nums, a))
            if b>maximum:
                maximum=b
            a= a[1:] + a[:1]

        return(maximum)
    
#3rd try(space optimized)
# Time: O(n^2), Space: O(1)

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:

        n = len(nums)

        maximum = float('-inf')

        for k in range(n):

            b = 0

            for i in range(n):

                b += i * nums[(i - k) % n]

            if b > maximum:
                maximum = b

        return maximum




        




        