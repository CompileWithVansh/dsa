#time complexity: O(n)
#space complexity: O(n)

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        n = len(A)

        visited = [0] * (n + 1)

        ans = []
        common = 0

        for i in range(n):

            visited[A[i]] += 1
            if visited[A[i]] == 2:
                common += 1

            visited[B[i]] += 1
            if visited[B[i]] == 2:
                common += 1

            ans.append(common)

        return ans