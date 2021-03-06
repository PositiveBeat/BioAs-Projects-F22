'''
Plotting csv files.

Author: Nicoline Louise Thomsen
'''

import csv as csv_libary
import matplotlib.pyplot as plt


class CSVprocessor():
    
    def __init__(self, filename, n_columns=2):
        self.filename = filename
        self.n_columns = n_columns

        self.data = self.get_data()


    def get_data(self):

        data = [[] for i in range(self.n_columns)]
        
        with open(self.filename,'r') as csvfileQuick:
            file = csv_libary.reader(csvfileQuick, delimiter=',')
            next(file)  # Skip first line / header
            for row in file:
                for i in range(self.n_columns):
                    data[i].append(row[i])

        return data

    
    def extract_float_columns(self, colum_ids):

        data = [[] for i in range(len(colum_ids))]

        for i, ID in enumerate(colum_ids):
            for j in range(len(self.data[ID])):
                data[i].append(float(self.data[ID][j]))

        return data
    
    
    def plot_float_data(self, title=None, xlabel='x', ylabel='y', ylim=None, column_name='none', style='r'):
        
        dataset = self.extract_float_columns(range(len(self.data)))
        t = dataset[0]
        data = dataset[1:]
        
        for i, column in enumerate(data):
            plt.plot(t, column, style, label = column_name + str(i), markersize=1)
    
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        
        if (title != None):
            plt.title(title)
        
        if (ylim != None):
            plt.ylim(ylim)
        
        if (column_name != 'none'):
            plt.legend()
        
        plt.show()



if __name__ == '__main__':

    # CSV = CSVprocessor('logs/data_boid9.csv', 2)
    CSV = CSVprocessor('logs/data_sync8.csv', 101)
    
    CSV.plot_float_data(xlabel='frame', ylabel='sync value', style='rx')
    # CSV.plot_float_data(xlabel='frame', ylabel='$\phi$', ylim=[0, 1.1])

