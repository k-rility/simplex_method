import copy


class SimplexMethod:
    def __init__(self, A, c, b):
        self.__A = A
        self.__c = c
        self.__b = b
        self.f = [-i for i in c]
        self.res = 0
        self.simplex_table = None
        self.ind_r = 0
        self.ind_c = 0
        self.pivot = 0
        self.old_simplex_table = copy.deepcopy(A)

    def init_simplex_table(self):
        self.f.append(self.res)
        A_copy = copy.copy(self.__A)
        A_copy.append(self.f)
        self.simplex_table = A_copy

    def init_old_simplex_table(self):
        self.old_simplex_table.append(copy.deepcopy(self.f))

    def perm_col(self):
        min_c = self.f[0]
        for i in range(len(self.__A)):
            flag = True
            for j in range(len(self.__A)):
                flag = self.__A[j][i] != 0
            if flag and self.f[i] <= min_c:
                min_c = self.f[i]
                self.ind_c = i

    def perm_row(self):
        min_r = self.__b[0] / self.__A[0][self.ind_c]
        for i in range(len(self.__A)):
            if self.__b[i] / self.__A[i][self.ind_c] <= min_r:
                min_r = self.__b[i] / self.__A[i][self.ind_c]
                self.ind_r = i

    def get_pivot(self):
        self.pivot = self.__A[self.ind_r][self.ind_c]

    def jordan_transform(self):
        for i in range(len(self.simplex_table)):
            self.simplex_table[self.ind_r][i] /= self.pivot
        for i in range(len(self.simplex_table[self.ind_r])):
            self.simplex_table[i][self.ind_c] /= (-self.pivot)
        self.simplex_table[self.ind_r][self.ind_c] = (-self.simplex_table[self.ind_r][self.ind_c])
        for i in range(len(self.simplex_table)):
            for j in range(len(self.simplex_table[0])):
                if i == self.ind_r or j == self.ind_c:
                    continue
                else:
                    self.simplex_table[i][j] = (self.pivot * self.simplex_table[i][j] -
                                                self.old_simplex_table[self.ind_r][j] *
                                                self.old_simplex_table[i][self.ind_c]) / self.pivot
        self.f = self.simplex_table[len(self.simplex_table) - 1]
        self.res = self.f[len(self.f) - 1]
        self.old_simplex_table = copy.deepcopy(self.simplex_table)
        for i in range(len(self.__A)):
            for j in range(len(self.__A[0])):
                self.__A[i][j] = self.simplex_table[i][j]

    def iteration(self):
        while min(self.f) < 0:
            self.perm_col()
            self.perm_row()
            self.get_pivot()
            self.jordan_transform()
