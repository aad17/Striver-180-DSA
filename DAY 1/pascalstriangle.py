'''
Generate a Pascal's Triangle
'''
class Solution:
    def generate(self, numRows: int):
        # Initialise a Output array as [[0, 1, 0]]
        op = [[0, 1, 0]]
        k = 0
        # Iterate while k is less than number of rows
        while k < numRows-1:
            # Initialise a temp array with 0
            temp = [0]
            i, j = 0, 1
            while j < len(op[k]):
                # Add the elements like in pascal's triangle
                temp.append(op[k][i] + op[k][j])
                # Increment i and j
                i += 1
                j += 1
            
            # Also add an element 0 for further processing
            # Thus array becomes [[0, 1, 0], [0, 1, 1, 0], [0, 1, 2, 1, 0], ....]
            temp.append(0)
            k += 1
            op.append(temp)
            
        # Remove the additional 0's from first position and last position 
        for lst in op:
            lst.pop(0)
            lst.pop()
            
        return op

s = Solution()
print(s.generate(5))