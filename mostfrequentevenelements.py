class Solution:
    def mostFrequentEven(self, nums):
        d={}
        for i in nums:
            if(i%2==0):
                try:
                    element = d[i]
                    d[i]=element+1
                except KeyError:
                    d[i]=1
        if(len(list(d.values()))==0):
            return -1
        maxCount=max(list(d.values()))
        maxElements=[]
        for key,value in d.items():
            if(value==maxCount):
                maxElements.append(key)
        return min(maxElements)
        

s=Solution()
print(s.mostFrequentEven([0,1,2,2,4,4,1]))