class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        l = [[1]]
        for row in range(2,numRows+1):
            last = l[-1]
            level_row = []
            for i in range(row):
                if i > 0 and i < len(last):
                    level_row.append(last[i]+last[i-1])
                else:
                    level_row.append(1)
            l.append(level_row)
        return l
