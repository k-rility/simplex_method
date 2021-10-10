import from_file
import simplex_method as sm

if __name__ == '__main__':
    A, c, b = from_file.get_data(open("input.txt", "r"))
    res = sm.SimplexMethod(A=A, c=c, b=b)
    print(res.A)
    print(res.f)
    print(res.perm_col())
    print(res.perm_row())
    # res.simplex_iteration()
    # smp = res.get_simplex_table()
    # print()
    # for i in range(len(smp)):
    #     print(smp[i])
    # print()
    # st = res.div_row_and_col()
    # for i in range(len(st)):
    #     print(st[i])

    print()

    jt = res.jordan_transform()
    for i in range(len(jt)):
        print(jt[i])
