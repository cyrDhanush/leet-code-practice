class Solution(object):

    def haveRepetition(self, listt):
        for i in listt:
            c=listt.count(i)
            if(c>1 and i!='.'):
                return True # repetitions found
        return False # no repetitions found

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool    
        """
        # checking rows
        for row in board:
            res=self.haveRepetition(row)
            if(res==True):
                return False
        # checking columns
        for r in range(0,9):
            newlist=[]
            for c in range(0,9):
                newlist.append(board[c][r])
            res=self.haveRepetition(newlist)
            if(res==True):
                return False
        # checking each box
        for a in range(0,3):
            for b in range(0,3):
                r1=(a*3)+0
                r2=(a*3)+3
                c1=(b*3)+0
                c2=(b*3)+3
                templist=[]
                for r in range(r1,r2):
                    for c in range(c1,c2):
                        element = board[c][r]
                        templist.append(element)
                res=self.haveRepetition(templist)
                if(res==True):
                    return False
        # no repetitions found
        return True



            
        
        
s=Solution()
f=s.isValidSudoku(
    [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
)
print(f)