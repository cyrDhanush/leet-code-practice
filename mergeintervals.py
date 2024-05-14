class Solution:
    def checkContinuity(self, nl1, nl2):
        sl=sorted([nl1,nl2])
        l1=sl[0]
        l2=sl[1]
        if(l2[0]<=l1[1]):
            start = l1[0] if(l1[0]<l2[0]) else l2[0]
            end = l1[1] if(l1[1]>l2[1]) else l2[1]
            return [start, end]
        else:
            return []

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        inters=(intervals.copy())
        i=0
        while (i<(len(inters)-1)):
            res = self.checkContinuity(inters[i], inters[i+1])
            if(len(res)!=0):
                inters.pop(i+1)
                inters.pop(i)
                inters.insert(i, res.copy())
            i+=1
        # lastone check
        try:
            if(len(inters)>1):
                res = self.checkContinuity(inters[len(inters)-2], inters[len(inters)-1])
                if(len(res)!=0):
                    inters.pop(len(inters)-1)
                    inters.pop(len(inters)-2)
                    inters.insert(len(inters)-2, res.copy())
        except:
            pass
        return inters



s=Solution()
# print(s.merge([[1,3],[2,6],[8,10],[15,18]]))
# print(s.merge([[1,4],[5,6]]))
# print(s.merge([[1,4],[0,2],[3,5]]))
# print(s.merge([[1,4],[0,4]]))
print(s.merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
# print(s.checkContinuity([8,10],[15,18]))
