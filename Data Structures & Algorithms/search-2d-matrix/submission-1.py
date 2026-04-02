class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0,  m*n -1

        while l <= r:
            q = (l+r)//2
            q_row, q_col = q//n, q%n
            
            if matrix[q_row][q_col] == target:
                return True 
            elif matrix[q_row][q_col] > target:
                r = q-1
            else:
                l = q+1
        return False


        