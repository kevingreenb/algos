class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r:
            mid = (r + l) // 2
            nr = mid // n
            nc = mid % n
            print(f"r {r} | l {l}")
            print(f"mid {mid} | nr {nr} | nc {nc}")
            if matrix[nr][nc] == target:
                return True
            elif matrix[nr][nc] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False
