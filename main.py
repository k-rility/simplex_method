import from_file
import SimplexMethod

if __name__ == '__main__':
    A, c, b = from_file.get_data(open("input.txt", "r"))
    res = SimplexMethod.SimplexMethod(A, c, b)
    res.__repr__()
    print()
    res.iteration()
