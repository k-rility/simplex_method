import from_file
import SimplexMethod

if __name__ == '__main__':
    A, c, b = from_file.get_data(open("input.txt", "r"))
    res = SimplexMethod.SimplexMethod(A, c, b)
    res.init_simplex_table()
    res.init_old_simplex_table()
    for i in range(len(res.simplex_table)):
        print(res.simplex_table[i])
    print()
    res.perm_col()
    res.perm_row()
    res.get_pivot()
    res.jordan_transform()

    res.perm_col()
    res.perm_row()
    res.get_pivot()
    res.jordan_transform()

    for i in range(len(res.simplex_table)):
        print(res.simplex_table[i])
    print()

    # print(res.f)
    # print(res.res)
