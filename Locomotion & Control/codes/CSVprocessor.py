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
    
    def plot_data_pos():
        pos = csv_pos.extract_float_columns([0])
        posdes = csv_posdes.extract_float_columns([0])
        

        plt.plot(pos[0], 'r', label = 'actual position')
        plt.plot(posdes[0], 'g', label = 'desired position')

        plt.xlabel('t')
        plt.ylabel('[rad]')
        plt.title('Position vs. Desired Position')
        # plt.ylim([-0.5, 0.5])
        plt.legend()
        plt.show()
        
    def plot_data_tau():
        tau = csv_tau.extract_float_columns([0])

        plt.plot(tau[0], 'b')

        plt.xlabel('t')
        plt.ylabel('tau')
        plt.title('Tau over time')
        # plt.ylim([-0.5, 0.5])
        plt.legend()
        plt.show()
    

    # const const imp
    # csv_pos = CSVprocessor('plots/post_con/const_imp/pos0.csv', 1)
    # csv_posdes = CSVprocessor('plots/post_con/const_imp/des_pos0.csv', 1)
    # csv_tau = CSVprocessor('plots/post_con/const_imp/tau0.csv', 1)
    
    # const ada imp
    # csv_pos = CSVprocessor('plots/post_con/ada_imp/pos0.csv', 1)
    # csv_posdes = CSVprocessor('plots/post_con/ada_imp/des_pos0.csv', 1)
    # csv_tau = CSVprocessor('plots/post_con/ada_imp/tau0.csv', 1)
    
    # Track const imp
    # csv_pos = CSVprocessor('plots/track/const_imp/pos0.csv', 1)
    # csv_posdes = CSVprocessor('plots/track/const_imp/des_pos0.csv', 1)
    # csv_tau = CSVprocessor('plots/track/const_imp/tau0.csv', 1)
    
    # Track ada imp
    # csv_pos = CSVprocessor('plots/track/ada_imp/pos0.csv', 1)
    # csv_posdes = CSVprocessor('plots/track/ada_imp/des_pos0.csv', 1)
    # csv_tau = CSVprocessor('plots/track/ada_imp/tau0.csv', 1)
    
    
    
    # plot_data_pos()
    plot_data_tau()
    
    


