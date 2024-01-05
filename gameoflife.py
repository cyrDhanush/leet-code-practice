class Solution(object):
    def getItem(self, matrix, r, c):
        item=0
        if(r<0 or c<0):
            return 0
        if(c>=len(matrix[0]) or r>=len(matrix)):
            return 0
        try:
            item=matrix[r][c]
        except IndexError:
            return 0
        return item
    def countNeighbours(self, matrix, r, c):
        neighbours=0
        #all tops
        neighbours+=self.getItem(matrix, r-1, c-1)
        neighbours+=self.getItem(matrix, r-1, c)
        neighbours+=self.getItem(matrix, r-1, c+1)
        #all bottoms
        neighbours+=self.getItem(matrix, r+1, c-1)
        neighbours+=self.getItem(matrix, r+1, c)
        neighbours+=self.getItem(matrix, r+1, c+1)
        #left (only 1)
        neighbours+=self.getItem(matrix, r, c-1)
        #right (only 1)
        neighbours+=self.getItem(matrix, r, c+1)
        return neighbours
    
    def predictNextState(self, current, neighbourCount):
        if(current==1):
            if(neighbourCount==2 or neighbourCount==3):
                return 1
            else:
                return 0
        else:
            if(neighbourCount==3):
                return 1
        return 0
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        nextState=[]
        # self.maxc=len(board[0])
        # self.maxr=len(board)
        #creating empty matrix
        for i in range(0, len(board)):
            nextState.append([*range(0,len(board[0]))])

        #processing
        for r in range(0,len(board)):
            for c in range(0,len(board[0])):
                neighbours=self.countNeighbours(board, r, c)
                nextState[r][c]=self.predictNextState(board.copy()[r][c], neighbours)
        board=nextState.copy()
        print(board)


s=Solution()
l=s.gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]])
print(l)