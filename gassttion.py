class Solution(object):
    def check(self, gas, cost, starting):
        index=starting
        l=len(gas)
        iteration=0  # can only from 0 to l
        currentGas=0
        while True:
            if(index>=l):
                index=0
            # do process here
            currentGas+=gas[index] #gas filled
            currentGas-=cost[index] #used to moving to next station
            if(iteration==(l-1)):
                # print(currentGas, cost[(index)])
                return True
            if(currentGas<=0):
                return False
            elif(iteration>=l):
                return False
            # within this box
            iteration+=1
            index+=1
        return False
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        # picking the starting point
        for i in range(0,len(gas)):
            if(gas[i]>cost[i]):
                res=self.check(gas, cost, i)
                if(res==True):
                    return i
                elif(res==False and (i==len(gas)-1)):
                    return -1
        return -1

s=Solution()
print(s.canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]))
print(s.canCompleteCircuit([2,3,4],[3,4,3]))
print(s.canCompleteCircuit([4,5,3,1,4],[5,4,3,4,2]))