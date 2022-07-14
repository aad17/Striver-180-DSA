# Brute Force approach
# Take another matrix of same size
# Copy the first row into last column, second row into second last column and so on


# Optimised
# Iterate through the matrix
# Step 1. Make a matrix transpose
#       a. By SWAP(matrix[i][j], matrix[j][i])
# Step 2. Reverse each row of the obtained matrix
class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Take the length of matrix
        n = len(matrix)

        # Iterate through the elements
        for i in range(n):
            for j in range(i):
                # Swap the elements to do the transpose
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for i in range(n):
            matrix[i].reverse()

        return matrix
                

s = Solution()
print(s.rotate([[1,2,3],[4,5,6],[7,8,9]]))