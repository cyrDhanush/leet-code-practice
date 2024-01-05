class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        maxn=len(matrix)
        rotatedMatrix=[]
        for i in range(maxn):
            slist=[]
            for j in range(maxn):
                slist.append(0)
            rotatedMatrix.append(slist)
        i,r=0,0

        while (i<maxn and r<maxn):
            c=maxn-1
            j=0
            while (j<maxn and c>-1):
                #process
                print(matrix)
                rotatedMatrix[i][j]=matrix[c][r]
                print(matrix)
                j+=1
                c-=1
            i+=1
            r+=1
        
        for r in range(0, maxn):
            for c in range(0, maxn):
                matrix[r][c]=rotatedMatrix[r][c]
                
        

s=Solution()
s.rotate([[1,2,3],[4,5,6],[7,8,9]])