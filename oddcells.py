class Solution:
    def oddCells(self, n, m, indices):
        import numpy as np
        matrix = np.zeros([n,m])
        print(matrix)
        for i in indices:
            print(matrix[i[0] , :])
            print(np.ones([1,m]))
            matrix[i[0] , :] = matrix[i[0],:] + np.ones([m])
            matrix[: , i[1]] = matrix[:,i[1]] + np.ones([n,1])
        count = 0
        for i in indices:
            for j in i:
                if not j % 2 ==0:
                    count +=1
        return count

    def oddCells1(self, n, m, indices):
        matrix = [[0 for I in range(m)] for J in range(n)]
        for i in indices:
            for l in range(m):
                matrix[i[0]][l] += 1
            for l in range(n):
                matrix[l][i[1]] +=1
        count = 0
        for i in range(n):
            for j in range(m):
                if not matrix[i][j] % 2 == 0:
                    count +=1
        return count


    print(oddCells1([],2,3,[[0,1],[1,1]]))