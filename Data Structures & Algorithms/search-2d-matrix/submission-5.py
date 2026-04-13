class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        def get_value(index):
            row = index // n
            column = index % n
            #print(index, row, column, m, n)
            return matrix[row][column] 

        low, high = 0, m*n-1

        while low <= high:
            mid = low + (high - low) // 2
            mid_val = get_value(mid)
            if mid_val == target:
                return True
            if mid_val < target:
               low = mid + 1
            else:
                high = mid - 1
        
        return False