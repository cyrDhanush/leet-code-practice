class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        #finding the storing the zeros columns and rows
        rows=[]
        columns=[]
        for r in range(0,len(matrix)):
            for c in range(0, len(matrix[0])):
                if matrix[r][c]==0:
                    rows.append(r)
                    columns.append(c)

        # making rows as zeros
        for i in rows:
            for c in range(0,len(matrix[0])):
                matrix[i][c]=0
        
        # making columns as zeros
        for i in columns:
            for r in range(0,len(matrix)):
                matrix[r][i]=0
        print(matrix)

s=Solution()
s.setZeroes([[1,1,1],[1,0,1],[1,1,1]])