class matrix:
    def __init__(self, ls1, ls2):
        self.ls1 = ls1
        self.ls2 = ls2

    def __add__(self):
        matrixx = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        for i in range(len(self.ls1)):
            for s in range(len(self.ls2[i])):
                matrixx[i][s] = self.ls1[i][s] + self.ls2[i][s]
        return str('\n'.join(['\t'.join([str(s) for s in i]) for i in matrixx]))
    def __str__(self):
        return str('\n'.join(['\t'.join([str(s) for s in i]) for i in matrixx]))

matrix_vvod = matrix([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]],
                   [[10, 9, 8],
                    [7, 6, 5],
                    [4, 3, 2]])



print(matrix_vvod.__add__())