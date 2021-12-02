import copy
import numpy as np
from prettytable import PrettyTable


class SimplexMethod:

    # в функции __init__ создаем матрицу из предоставленных данных, которая будет символизировать симплекс таблицу и с
    # через нее же будем находить опорную симплекс таблицу и оптимальные решения

    def __init__(self, A, c, b, MinMax):
        self.MinMax = MinMax

        # создаем временную матрицу, в которую добавим все данные
        temp = A
        for i in range(len(temp)):
            temp[i].append(b[i])
        temp.append(c)
        temp[len(temp) - 1].append(0)

        # копируем ту же матрицу как матрицу из модуля numpy

        self.SimplexTable = np.matrix(temp)

        # запоминаем количество строк и столбов в этой матрице, чтобы избежать ищлишне большого кода

        self.RowNum, self.ColNum = self.SimplexTable.shape
        # self.SimplexTable[self.RowNum - 1] *= -1

        # это матрица, которая будет соответствовать матрице не подвергающаяся изменениям через Жордановы преобразования

        self.OldSimplexTable = copy.deepcopy(self.SimplexTable)

        # индексы разрешающего элемента в матрице

        self.IdxRow = 0
        self.IdxCol = 0

        # поля для более понятного представления симплекс таблицы

        self.Headers = [''] + [f'x{i}' for i in range(1, self.ColNum)] + ['C']
        self.BaseCol = [[f'u{i}'] for i in range(1, self.RowNum)] + [['F']]

    # функция ниже возвращает значение разрешающего элемента обращаясь к нему через определенные ранее индексы

    def get_pivot(self):
        return self.SimplexTable[self.IdxRow, self.IdxCol]

    # преобразовываем элементы матрице через функцию ниже

    def jordan_transform(self):

        # находим значение разрешающего элемента

        pivot = self.get_pivot()

        # делим разрешающую строку на разрешающий элемент

        self.SimplexTable[self.IdxRow] /= pivot

        # делим разрешающий столбец на разрешающий элемент, взятый со знаком минус

        self.SimplexTable[:, self.IdxCol] /= -pivot

        # также домножаем разрешающий элемент, находящийся в матрице на минус единицу, чтобы в связи с преобразованиями
        # произведенными выше, он не изменил свой знак

        self.SimplexTable[self.IdxRow, self.IdxCol] *= -1

        # преобразовываем элементы матрицы, которые не входят в разрешающий столбец и разрешающую строку

        for i in range(self.RowNum):
            for j in range(self.ColNum):

                # если элемент состоит в разрещающей строке или столбце, то продолжаем поиск тех элементов, которые туда
                # не входят

                if i == self.IdxRow or j == self.IdxCol:
                    continue
                else:

                    # если нашли такие элементы, то преобразовываем их по формуле

                    self.SimplexTable[i, j] = (pivot * self.SimplexTable[i, j] -
                                               self.OldSimplexTable[self.IdxRow, j] *
                                               self.OldSimplexTable[i, self.IdxCol]) / pivot

        self.OldSimplexTable = copy.deepcopy(self.SimplexTable)

    # функция для проверки неотрицательности свободных членов

    def check_free_members(self):
        flag = True
        for i in range(self.RowNum - 1):
            if self.SimplexTable[i, self.ColNum - 1] < 0:
                flag = False
                break
        return flag

    # функция для поиска разрешающего столбца

    def ref_perm_col(self):
        if self.SimplexTable[0:self.RowNum - 1, self.ColNum - 1].min() < 0:
            self.IdxCol = self.SimplexTable[0:self.RowNum - 1, self.ColNum - 1].argmin()

    def ref_perm_row(self):
        MinRowArg = None

        for i in range(self.RowNum - 1):
            flag = self.SimplexTable[i, self.IdxCol] != 0
            if MinRowArg == None and flag and self.SimplexTable[i, self.ColNum - 1] / self.SimplexTable[
                i, self.IdxCol] > 0:
                MinRowArg = self.SimplexTable[i, self.ColNum - 1] / self.SimplexTable[i, self.IdxCol]
                self.IdxRow = i
            elif flag and self.SimplexTable[i, self.ColNum - 1] / self.SimplexTable[i, self.IdxCol] > 0 and \
                    self.SimplexTable[i, self.ColNum - 1] / self.SimplexTable[i, self.IdxCol] <= MinRowArg:
                MinRowArg = self.SimplexTable[i, self.ColNum - 1] / self.SimplexTable[i, self.IdxCol]
                self.IdxRow = i

    # функция для поиска опорного решения, совмещающая в себе все функции описанные выше

    def ref_solution(self):
        iteration = 1
        while not self.check_free_members():
            self.ref_perm_col()
            self.ref_perm_row()
            self.jordan_transform()
            print()
            print(self.SimplexTable)
            print(f'iteration: {iteration}')
            print("permission col: ", self.IdxCol)
            print("permission row: ", self.IdxRow)
            iteration += 1

        # функция для поиска оптимального решения, которая вызывается при нахождении оптимального решения

        self.optimal()

    def check_obj_func(self):
        flag = True
        for i in range(self.ColNum - 1):
            if self.SimplexTable[self.RowNum - 1, i] > 0:
                flag = False
                break
        return flag

    def perm_col(self):
        if self.SimplexTable[self.RowNum - 1, 0:self.ColNum - 1].max() > 0:
            self.IdxCol = self.SimplexTable[self.RowNum - 1, 0:self.ColNum - 1].argmax()

    # функция для поиска оптимального решения

    def optimal(self):
        iteration = 1
        self.print_table()

        while not self.check_obj_func():
            self.perm_col()
            self.ref_perm_row()
            self.jordan_transform()
            print()

            temp = self.BaseCol[self.IdxRow]
            self.BaseCol[self.IdxRow] = [self.Headers[self.IdxCol + 1]]
            self.Headers[self.IdxCol + 1] = temp[0]
            self.print_table()

            print(f'iteration: {iteration}')
            print("permission col: ", self.IdxCol)
            print("permission row: ", self.IdxRow)
            iteration += 1

    def print_table(self):
        ReprTable = PrettyTable()
        ReprTable.field_names = self.Headers
        for i in range(self.RowNum):
            if i == self.RowNum - 1:
                ReprTable.add_row(self.BaseCol[len(self.BaseCol) - 1] + np.array(self.SimplexTable)[i].tolist())
            else:
                ReprTable.add_row(self.BaseCol[i] + np.array(self.SimplexTable)[i].tolist())
        return print(ReprTable)
