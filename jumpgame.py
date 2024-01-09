class Solution:
    def findNextMax(self, nums, currentIndex, exceptionIndices):
        currentNumber=nums[currentIndex]
        maxNumber=0
        maxNumberIndex=-2
        nextRange=currentNumber
        if(currentIndex==len(nums)-1):
            return -1
        if(nums[currentIndex]>=(len(nums)-1)):
            return -1
        if(currentNumber+currentIndex>=len(nums)):
            nextRange=len(nums)-(currentIndex+1)

        for i in range(currentIndex+1, currentIndex+nextRange+1):
            if i in exceptionIndices:
                # don't do it
                pass
            elif(nums[i]>=maxNumber):
                maxNumber=nums[i]
                maxNumberIndex=i
        return maxNumberIndex
    
    def findExceptions(self, nums):
        exceptionIndices=[]
        for i in range(len(nums)):
            if(nums[i]==0):
                pass
            else:
                l=i+1
                r=i+1+nums[i]
                if(r>=len(nums)):
                    r=len(nums)-1
                else:
                    tempList=nums[l:r]
                    if(tempList==([0]*len(tempList)) and len(tempList)!=0):
                        exceptionIndices.append(i)
        return exceptionIndices
    def canJump(self, nums: list[int]) -> bool:
        index=0
        exceptionIndices=self.findExceptions(nums)
        while index<len(nums):
            if(nums[index]==0 and index!=len(nums)-1):
                return False
            if(index>=(len(nums)-1)):
                return True
            nextIndex = self.findNextMax(nums, index, exceptionIndices)
            if(nextIndex==-1):
                return True
            else:
                index=nextIndex
                print(nums[index],((len(nums)-1)-index))
                if(nums[index]>=((len(nums)-1)-index)):
                    return True
        return False


s=Solution()
# print(s.canJump([2,3,1,1,4]))
# print(s.canJump([3,2,1,0,4]))
# print(s.canJump([3,0,8,2,0,0,1]))
# print(s.canJump([4,2,0,0,1,1,4,4,4,0,4,0]))
# print(s.canJump([2,5,0,0]))
print(s.canJump([1,1,0,1]))
# print(s.findNextMax([2,3,1,1,4],2))