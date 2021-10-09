import numpy as np


def get_data(file):
    data = []
    c = []
    b = []
    lines = [line.replace('\n', '') for line in file]
    for line in lines:
        if 'c=' in line:
            c = [float(i) for i in line[line.find('[') + 1:line.find(']')].split()]
        elif 'b=' in line:
            b = [float(i) for i in line[line.find('[') + 1:line.find(']')].split()]
            for j in range(len(b)):
                data[j].append(b[j])
        else:
            data.append([float(i) for i in line[line.find('[') + 1:line.find(']')].split()])
    A = np.array(data, dtype=np.float)
    return A, c, b
