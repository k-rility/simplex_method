import numpy as np


def get_lines(file):
    A_temp = []
    c = []
    b = []
    lines = [line.replace('\n', '') for line in file]
    for line in lines:
        if 'c=' in line:
            c = [float(i) for i in line[line.find('[') + 1:line.find(']')].split()]
        elif 'b=' in line:
            b = [float(i) for i in line[line.find('[') + 1:line.find(']')].split()]
        else:
            A_temp.append([float(i) for i in line[line.find('[') + 1:line.find(']')].split()])
    A = np.array(A_temp, dtype=np.float)
    return A, c, b
