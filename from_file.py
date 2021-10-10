import numpy as np


def get_data(file):
    A = []
    c = []
    b = []
    lines = [line.replace('\n', '') for line in file]
    for line in lines:
        if 'c=' in line:
            c = [float(i) for i in line[line.find('[') + 1:line.find(']')].split()]
        elif 'b=' in line:
            b = [float(i) for i in line[line.find('[') + 1:line.find(']')].split()]
            for j in range(len(b)):
                A[j].append(b[j])
        else:
            A.append([float(i) for i in line[line.find('[') + 1:line.find(']')].split()])
    return A, c, b
