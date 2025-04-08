import numpy as np
import matplotlib.pyplot as plt
import scipy
def import_file(file):
    with open('C:\\Users\\tommy\\OneDrive\\Documents\\Advanced lab\\Lab data\\' + file, 'rb') as f:
        data = f.read()
        data = [bin(x) for x in data]
        data = data[:7989*4:4]
        for i in range (len(data)):

            if data[i] == (''):
                data[i]='0'
            data[i] = int(data[i], 2)
    return data


