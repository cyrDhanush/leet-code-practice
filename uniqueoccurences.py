class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        arr.sort()
        occ=[]
        i=0
        while i<len(arr):
            c=arr.count(arr[i])
            if(c in occ):
                return False
            else:
                occ.append(c)
            i+=(c)
        return True
        
s=Solution()
print(s.uniqueOccurrences([1,2,2,1,1,3]))
print(s.uniqueOccurrences([1,2]))
print(s.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]))