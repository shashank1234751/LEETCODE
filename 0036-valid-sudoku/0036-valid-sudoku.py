class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                nums=board[i][j]
                box = (i // 3) * 3 + (j // 3)
                if nums in rows[i]:
                    return False
                if nums in cols[j]:
                    return False
                if nums in boxes[box]:
                    return False
                rows[i].add(nums)
                cols[j].add(nums)
                boxes[box].add(nums)
        return True