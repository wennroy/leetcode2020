class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        if obstacleGrid == []:
            return []
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        used = []
        [used.append([0] * n) for _ in range(m)]

        px = [1, 0]
        py = [0, 1]

        def dfs(self, i, j):
            if used[i][j] == 1 or obstacleGrid[i][j] == 1:
                return []
            elif i == m - 1 and j == n - 1:
                return [[m - 1, n - 1]]
            else:
                used[i][j] = 1
                for k in range(2):
                    x = px[k] + i
                    y = py[k] + j
                    if x < 0 or x >= m or y < 0 or y >= n:
                        continue
                    else:
                        next_step = dfs(self, x, y)
                        if next_step == []:
                            continue
                        else:
                            step = []
                            step.append([i, j])
                            [step.append(_) for _ in next_step]
                            return step
                return []

        step = dfs(self, 0, 0)
        return step
