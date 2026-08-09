class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        for n in range(0,len(matrix)):
            if target in matrix[n]:
                return True
        return False
