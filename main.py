import from_file
import SimplexMethod

if __name__ == '__main__':
    A, c, b = from_file.get_data(open("input.txt", "r"))
    res = SimplexMethod.SimplexMethod(A, c, b)
    for i in range(len(res.simplex_table)):
        print(res.simplex_table[i])
    print()
    res.iteration()
    # for i in range(len(res.simplex_table)):
    #     print(res.simplex_table[i])
    # print(res.__repr__())
