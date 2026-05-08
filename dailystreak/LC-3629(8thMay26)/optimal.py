#time complexity: O(n log n)    
# space complexity: O(n log n) for storing prime factors of numbers up to 10^6

MAXN = 1_000_001

primeFactors = [[] for _ in range(MAXN)]

for prime in range(2, MAXN):

    if not primeFactors[prime]:

        for multiple in range(prime, MAXN, prime):
            primeFactors[multiple].append(prime)


class Solution:

    def minJumps(self, nums: List[int]) -> int:

        n = len(nums)

        primeToIndices = defaultdict(list)

        # store indices of prime numbers
        for index, value in enumerate(nums):

            if len(primeFactors[value]) == 1:
                primeToIndices[value].append(index)

        steps = 0

        visited = [False] * n
        visited[n - 1] = True

        queue = [n - 1]

        while True:

            nextQueue = []

            for index in queue:

                if index == 0:
                    return steps

                # left jump
                if index > 0 and not visited[index - 1]:

                    visited[index - 1] = True
                    nextQueue.append(index - 1)

                # right jump
                if index < n - 1 and not visited[index + 1]:

                    visited[index + 1] = True
                    nextQueue.append(index + 1)

                # teleport jumps
                for prime in primeFactors[nums[index]]:

                    for nextIndex in primeToIndices[prime]:

                        if not visited[nextIndex]:

                            visited[nextIndex] = True
                            nextQueue.append(nextIndex)

                    primeToIndices[prime].clear()

            queue = nextQueue
            steps += 1