import numpy as np


class SimplexMethod:
    def __init__(self, A, c, b):
        self.A = A
        self.c = c
        self.b = b
        self.f = [-i for i in c]
        self.res = 0
        self.r = 0
        self.c = 0
        self.pivot = 0

    def perm_col(self):
        col = []
        min_c = self.f[0]
        ind = 0
        for i in range(len(self.A)):
            flag = True
            for j in range(len(self.A)):
                flag = self.A[j][i] != 0
            if flag and self.f[i] <= min_c:
                min_c = self.f[i]
                ind = i

        for i in range(len(self.A)):
            col.append(self.A[i][ind])
        self.c = ind
        return col

    def perm_row(self):
        row = []
        min_r = self.b[0] / self.perm_col()[0]
        ind = 0
        for i in range(len(self.perm_col())):
            if self.b[i] / self.perm_col()[i] <= min_r:
                min_r = self.b[i] / self.perm_col()[i]
                ind = i
        for i in range(len(self.A)):
            row.append(self.A[ind][i])
        self.r = ind
        return row

    def get_pivot(self):
        self.pivot = self.A[self.r][self.c]
        return self.pivot

    def get_simplex_table(self):
        self.f.append(self.res)
        self.A.append(self.f)
        simplex_table = self.A
        return simplex_table

    def div_row_and_col(self):
        self.get_pivot()
        st = self.get_simplex_table()
        for i in range(len(self.A[self.r])):
            st[self.r][i] /= self.pivot
        for i in range(len(self.A[self.c])):
            st[i][self.c] /= (-self.pivot)
        st[self.r][self.c] = (-st[self.r][self.c])
        return st

    def jordan_transform(self):
        st = self.get_simplex_table()
        for i in range(len(st[self.r])):
            for j in range(len(st[self.c])):
                if i == self.r or j == self.c:
                    continue
                else:
                    ind_1 = st[self.r][i]
                    ind_2 = st[i][self.c]
                    st[i][j] = (self.pivot * st[i][j] - st[self.r][i] * st[i][self.c]) / self.get_pivot()
        return st
