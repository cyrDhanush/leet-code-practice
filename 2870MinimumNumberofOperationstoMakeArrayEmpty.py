class Solution(object):
    def minOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #count of each numbers
        countedNumbers=[]
        counts=[]
        operations=0
        for i in nums:
            if i not in countedNumbers:
                c = nums.count(i)
                counts.append(c)
                countedNumbers.append(i)
        print(counts)
        for i in counts:
            currentOperation=0
            if(i==1):
                return -1
            if(i<=3):
                currentOperation+=1
            else:
                if(i%3==0):
                    currentOperation+=int(i/3)
                elif(i%3==1):
                    if(i%2==0):
                        currentOperation+=int(i/2)
                elif((i%3)%2==0):
                    currentOperation+=int(i/3)
                    currentOperation+=int((i%3)/2)
                elif(i%2==0):
                    currentOperation+=int(i/2)
                else:
                    return -1
            operations+=currentOperation



        return operations
        

s=Solution()
print(s.minOperations([14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]))

