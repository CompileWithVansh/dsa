#time complexity: O(n^2)
#space complexity: O(n)



class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        
        setA = set()
        setB = set()
        
        ans = []
        
        for i in range(n):
            setA.add(A[i])
            setB.add(B[i])
            
            count = 0
            
            for num in setA:
                if num in setB:
                    count += 1
            
            ans.append(count)
        
        return ans