class SimplexMethod:
    def __init__(self, A, c, b):
        self.A = A
        self.c = c
        self.b = b

    def get_f(self):
        f = []
        temp = 0
        for i in range(self.A.shape[0]):
            for j in range(self.A.shape[1]):
                temp = (0 * self.A[j][i])
            temp -= self.c[i]
            f.append(temp)
        return f

    def get_min(self):
        f = self.get_f()
        min_c = f[0]
        ind_c = 0
        for i in range(self.A.shape[0]):
            flag = True
            for j in range(self.A.shape[1]):
                flag = self.A[j][i] != 0
            if flag and f[i] <= min_c:
                min_c = f[i]
                ind_c = i

        return ind_c

    def get_pivot(self):
        ind_r = 0
        pivot = self.b[0]
        for i in range(self.A.shape[0]):
            if self.b[i] / self.A[i][self.get_min()] < pivot:
                pivot = self.A[i][self.get_min()] / self.b[i]
                ind_r = i
        return self.A[self.get_min()][ind_r]
