import from_file
import simplex_method as sm

if __name__ == '__main__':
    A, c, b = from_file.get_data(open("input.txt", "r"))
    res = sm.SimplexMethod(A=A, c=c, b=b)
    print(res.A)
    print(res.f)
    print(res.perm_col())
    print(res.perm_row())
    res.simplex_iteration()
    print(res.A)
    # print(res.get_simplex_table())
    # f = res.get_f()
    # print(res.get_min())
    # print(f)
    # print(res.get_pivot())
