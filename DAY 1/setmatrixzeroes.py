class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Take 2 lists as row and column lists
        - Traverse the row list and make the elements in the particular row as 0 where
        the row list element is 1
        - Traverse the column list and make the elements in the particular column as 0 
        where the column list element is 1
        """
        n, m = len(matrix), len(matrix[0])

        # Initialise 2 lists(row and column) as 0
        row, col = [0] * m, [0] * n
        
        # Traverse the matrix
        for i in range(n):
            for j in range(m):
                # If 0 is found make row and column element as 1
                if matrix[i][j] == 0:
                    row[j] = 1
                    col[i] = 1
                    
        # Traverse the row
        # Where the element is found to be 1
        # Make that perticular row 0
        for i in range(len(row)):
            if row[i] == 1:
                for l in range(n):
                    matrix[l][i] = 0
        
        # Traverse the column
        # Where the element is found to be 1
        # Make that perticular column 0
        for i in range(len(col)):
            if col[i] == 1:
                for l in range(m):
                    matrix[i][l] = 0

        return matrix

s = Solution()
print(s.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))