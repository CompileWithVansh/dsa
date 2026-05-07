#just first appproch using ,dfs checking each possible outcome 
#time complexity o(n^3)  very slow 
#GIVES TLE error on leetcode

class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        
        def dfs(i, visited):
            maximum = nums[i]

            for j in range(n):
                #move right 
                if j > i and nums[j] < nums[i]:
                    if j not in visited:
                        visited.add(j)
                        maximum = max(maximum, dfs(j, visited))

                # move left 
                elif j < i and nums[j] > nums[i]:
                    if j not in visited:
                        visited.add(j)
                        maximum = max(maximum, dfs(j, visited))

            return maximum

        for i in range(n):
            visited = set([i])
            ans.append(dfs(i, visited))

        return ans
    


#TRY 2 USING DEQUEUE BFS STILL TIME COMPLEXITY O(N^3)
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []

        for start in range(n):

            queue = deque([start])
            visited = set([start])

            maximum = nums[start]

            while queue:

                i = queue.popleft()

                # check all indexes
                for j in range(n):

                    # move right \
                    if j > i and nums[j] < nums[i]:

                        if j not in visited:
                            visited.add(j)
                            queue.append(j)

                            maximum = max(maximum, nums[j])

                    # move left 
                    elif j < i and nums[j] > nums[i]:

                        if j not in visited:
                            visited.add(j)
                            queue.append(j)

                            maximum = max(maximum, nums[j])

            ans.append(maximum)

        return ans
    
#TRY 3 TRYING TO FIND AND CREATE BFS GRAPH AND THEN TRAVERSING 
# IT USING DEQUEUE BFS TIME COMPLEXITY O(N^2)
#still TLE error on leetcode but better than previous two approaches
#TLE BECAUSE 10*10 OPERATION IS STILL IMMPOSIBLE 
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)


        graph = [[] for _ in range(n)]

        # build graph
        for i in range(n):
            for j in range(n):

                # move right
                if j > i and nums[j] < nums[i]:
                    graph[i].append(j)

                # move left
                elif j < i and nums[j] > nums[i]:
                    graph[i].append(j)

        ans = []

        # BFS from every node
        for start in range(n):

            queue = deque([start])
            visited = set([start])

            maximum = nums[start]

            while queue:

                node = queue.popleft()

                for nei in graph[node]:

                    if nei not in visited:

                        visited.add(nei)
                        queue.append(nei)

                        maximum = max(maximum, nums[nei])

            ans.append(maximum)

        return ans