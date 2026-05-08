#time O(n*sqrt(max(nums))) space O(n)   


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        mp = defaultdict(list)

        def prime(x):
            if x < 2:
                return 0
            i = 2
            while i * i <= x:
                if x % i == 0:
                    return 0
                i += 1
            return 1

        for i, x in enumerate(nums):
            d = 2
            while d * d <= x:
                if x % d == 0:
                    mp[d].append(i)
                    while x % d == 0:
                        x //= d
                d += 1
            if x > 1:
                mp[x].append(i)

        q = deque([0])
        vis = {0}
        used = set()
        ans = 0

        while q:
            for _ in range(len(q)):
                i = q.popleft()

                if i == n - 1:
                    return ans

                for j in (i - 1, i + 1):
                    if 0 <= j < n and j not in vis:
                        vis.add(j)
                        q.append(j)

                if prime(nums[i]) and nums[i] not in used:
                    for j in mp[nums[i]]:
                        if j not in vis:
                            vis.add(j)
                            q.append(j)
                    used.add(nums[i])

            ans += 1