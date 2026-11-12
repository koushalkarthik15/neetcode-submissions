class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n=len(matrix)
        for r in range(n):
            for c in range(r+1,n):
                matrix[r][c],matrix[c][r]=matrix[c][r],matrix[r][c]
        for row in matrix:
            left=0
            right=n-1
            while left<right:
                row[left],row[right]=row[right],row[left]
                left+=1
                right-=1