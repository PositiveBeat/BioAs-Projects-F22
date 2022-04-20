'''
Plotting csv files.

Author: Nicoline Louise Thomsen
'''

import csv
import matplotlib.pyplot as plt

t = []
data = []

def plotCSV(filename):
    
    with open(filename,'r') as csvfileQuick:
        plots = csv.reader(csvfileQuick, delimiter=',')
        next(plots)
        for row in plots:
            t.append(int(row[0]))
            data.append(float(row[1]))

    plt.plot(t, data)
    plt.xlabel('Time steps')
    plt.ylabel('Average heading [rad]')
    plt.title('Average heading over time')
    # plt.legend()
    
    plt.show()
    


if __name__ == '__main__':
    plotCSV('logs/data_30.csv')