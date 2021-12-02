import from_input
import SimplexMethod
import copy

if __name__ == '__main__':
    A, c, b, MinMax = from_input.get_data(open("input.txt", "r"))
    res = SimplexMethod.SimplexMethod(A, c, b, MinMax)
    # print(res.ref_perm_col())
    # print(res.ref_perm_row())
    res.ref_solution()
    # print(res.SimplexTable)
    # print(res.ref_perm_row())
    # print(res.SimplexTable[:, res.ColNum - 1])
    # print()
    # a = int(min(res.SimplexTable[:, res.ColNum - 1]))
    # print(a)

    # res.__repr__()
    # print()
    # res.iteration()
