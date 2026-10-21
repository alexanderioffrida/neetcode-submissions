class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for n in range(numRows):
            row = [1] * (n + 1)
            for k in range(1, n):
                row[k] = res[n - 1][k - 1] + res[n - 1][k]
            res.append(row)
        return res