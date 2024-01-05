class Solution(object):
    def changeOrder(self, currentOrder):
        if(currentOrder=='c++'):
            return 'r++'
        elif(currentOrder=='r++'):
            return 'c--'
        elif(currentOrder=='c--'):
            return 'r--'
        elif(currentOrder=='r--'):
            return 'c++'
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        mainlist=[]
        #used to store all the element indices
        elementaddresses=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                elementaddresses.append((i,j))
        # order c++, r++, c--, r--
        r=0
        c=0
        maxr=len(matrix)
        maxc=len(matrix[0])
        currentOrder='c++'
        elementaddresses.remove((0,0))
        lflag=False

        if(len(matrix)==1):
            return matrix[0]

        while len(elementaddresses)!=0:
            
            # checking max len -- only used once
            if(c==(maxc-1) and r==0):
                currentOrder=self.changeOrder(currentOrder)
            elif(r==(maxr-1) and c==0):
                currentOrder=self.changeOrder(currentOrder)
            elif(c==(maxc-1) and r==(maxr-1)):
                currentOrder=self.changeOrder(currentOrder)
            # element=matrix[r][c]
            if(lflag==False):
                # print(matrix[r][c])
                mainlist.append(matrix[r][c])
            else:
                #used to skipping the undoing changed element
                lflag=False
            # print(element)
            if(currentOrder=='c++'):
                c+=1
            elif(currentOrder=='c--'):
                c-=1
            elif(currentOrder=='r++'):
                r+=1
            elif(currentOrder=='r--'):
                r-=1
            
            # checking in element address
            if((r,c) in elementaddresses):
                elementaddresses.remove((r,c))
            else:
                #undoing the change
                lflag=True
                if(currentOrder=='c++'):
                    c-=1
                elif(currentOrder=='c--'):
                    c+=1
                elif(currentOrder=='r++'):
                    r-=1
                elif(currentOrder=='r--'):
                    r+=1
                # then changing order
                currentOrder=self.changeOrder(currentOrder)
        mainlist.append(matrix[r][c]) #appending the last element
        return mainlist
         


s=Solution()
print(s.spiralOrder([[2,3]]))