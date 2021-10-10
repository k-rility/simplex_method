import copy


class SimplexMethod:

    def __init__(self, A, c, b):
        self.simplex_table = A
        for i in range(len(self.simplex_table)):
            self.simplex_table[i].append(b[i])
        self.simplex_table.append([-i for i in c])
        self.simplex_table[len(self.simplex_table) - 1].append(0)

        self.old_simplex_table = copy.deepcopy(self.simplex_table)
        self.ind_row = 0
        self.ind_col = 0

    def perm_col(self):
        min_c = self.simplex_table[len(self.simplex_table) - 1][0]
        for i in range(len(self.simplex_table) - 1):
            if self.simplex_table[len(self.simplex_table) - 1][i] <= min_c:
                min_c = self.simplex_table[len(self.simplex_table) - 1][i]
                self.ind_col = i

    def perm_row(self):
        min_r = self.simplex_table[0][len(self.simplex_table[0]) - 1] / self.simplex_table[0][self.ind_col]
        for i in range(len(self.simplex_table) - 1):
            flag = self.simplex_table[i][self.ind_col] != 0
            if self.simplex_table[i][
                self.ind_col] > 0 and flag and self.simplex_table[i][len(self.simplex_table) - 1] / \
                    self.simplex_table[i][
                        self.ind_col] <= min_r:
                min_r = self.simplex_table[i][len(self.simplex_table) - 1] / self.simplex_table[i][self.ind_col]
                self.ind_row = i

    def get_pivot(self):
        return self.simplex_table[self.ind_row][self.ind_col]

    def jordan_transform(self):
        pivot = self.get_pivot()
        for i in range(len(self.simplex_table[0])):
            self.simplex_table[self.ind_row][i] /= pivot
        for i in range(len(self.simplex_table)):
            self.simplex_table[i][self.ind_col] /= -pivot
        self.simplex_table[self.ind_row][self.ind_col] = -self.simplex_table[self.ind_row][self.ind_col]

        for i in range(len(self.simplex_table)):
            for j in range(len(self.simplex_table[0])):
                if i == self.ind_row or j == self.ind_col:
                    continue
                else:
                    self.simplex_table[i][j] = (pivot * self.simplex_table[i][j] -
                                                self.old_simplex_table[self.ind_row][j] *
                                                self.old_simplex_table[i][self.ind_col]) / pivot

        self.old_simplex_table = copy.deepcopy(self.simplex_table)

    def iteration(self):
        while min(self.simplex_table[len(self.simplex_table) - 1]) < 0:
            self.perm_col()
            self.perm_row()
            self.jordan_transform()
