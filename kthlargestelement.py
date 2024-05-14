class Solution:
    biggestElements=[]
    def __init__(self):
        self.biggestElements=[]
    def insertAtLeast(self, number):
        if(number>self.biggestElements[0]):
            self.biggestElements.insert(0,number)
            self.biggestElements.pop(len(self.biggestElements)-1)
            return
        for i in range(0, len(self.biggestElements)-1):
            if(self.biggestElements[i]==number):
                self.biggestElements.insert(i+1, number)
                #to remove last number
                self.biggestElements.pop(len(self.biggestElements)-1)
                return 
            if(self.biggestElements[i]>number and self.biggestElements[i+1]<number):
                self.biggestElements.insert(i+1, number)
                #to remove last number
                self.biggestElements.pop(len(self.biggestElements)-1)
                return 
        if (0 in self.biggestElements):
            for n in range(0,len(self.biggestElements)):
                if(self.biggestElements[n]==0):
                    self.biggestElements[n]=number
                    return
        if(self.biggestElements[len(self.biggestElements)-1]<number):
            self.biggestElements[len(self.biggestElements)-1]=number
            return 
                
 
        
    def findKthLargest(self, nums, k):
        self.biggestElements.clear()
        for i in range(k):
            self.biggestElements.append(0)
        for i in nums:
            self.insertAtLeast(i)
            print(i)
            print(self.biggestElements)
        return (self.biggestElements[k-1])
        
        
        
        
        

s=Solution()
s.findKthLargest([3,2,1,5,6,4], 2)
s.findKthLargest([3,2,3,1,2,4,5,5,6], 4)
# s.findKthLargest([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,91,92,93,94,95,96,97,98,99], 10)
# s.findKthLargest([24,408,904,680,577,832,955,957,123,118,588,376,531,637,305,363,488,929,667,511,285,441,448,406,578,487,770,734,129,984,404,453,921,532,971,797,735,236,133],10)
