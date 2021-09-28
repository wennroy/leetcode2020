
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        n = len(machines)
        average = total/n
        if not isinstance(average, int):
            return -1
        