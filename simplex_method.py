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
        for i in range(self.A.shape[0]):
            flag = True
            for j in range(self.A.shape[0]):
                flag = self.A[j][i] != 0
            if flag and self.f[i] <= min_c:
                min_c = self.f[i]
                ind = i

        for i in range(self.A.shape[0]):
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
        for i in range(self.A.shape[0]):
            row.append(self.A[ind][i])
        self.r = ind
        return row

    def get_pivot(self):
        self.pivot = self.A[self.r][self.c]
        return self.pivot

    def simplex_iteration(self):
        self.get_pivot()
        self.A[self.r] = [(i / self.pivot) for i in self.A[self.r]]
