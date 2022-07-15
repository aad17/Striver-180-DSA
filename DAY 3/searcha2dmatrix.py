'''
Use binary search over the matrix
Consider each element place as number
e.g. [[1, 3, 5, 7], [10, 11, 16, 20],[23, 30, 34, 60]] as
[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]]
To find the position of mid element use the formula
i = int(mid/m)
j = mid % m
Where m is the number of elements in a single row of the matrix
'''

import math
class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        # Find the length of rows and columns of the matrix
        n, m = len(matrix), len(matrix[0])
        # Initialise the start and end to first and last element
        start, end = 0, (n*m)-1
        # Iterate
        while start <= end:
            # Calculate mid
            mid = math.ceil((start+end)/2)
            # Use of formula to find the index of perticular place in a matrix
            i, j = int((mid)/m), (mid) % m
            # Typical Binary Search
            if i < 0:
                i = (mid % m) - 1
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                end = mid-1
            else:
                start = mid+1

        return False

s = Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))