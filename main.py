import from_file
import simplex_method as sm

if __name__ == '__main__':
    A, c, b = from_file.get_lines(open("input.txt", "r"))
    print(A)
    print(c)
    print(b)
    res = sm.SimplexMethod(A=A, c=c, b=b)
    f = res.get_f()
    print(res.get_min())
    # print(f)
    # print(res.get_pivot())
