import numpy as np 
import csv
import seaborn as sns
import matplotlib.pyplot as plt
from random import randint

from classical.Periodogram import Periodogram
from classical.AveragedPeriodogram import AveragedPeriodogram
from classical.BlackmanTukey import BlackmanTukey
from parametric.AutocorrelationMethod import AutocorrelationMethod
from parametric.CovarianceMethod import CovarianceMethod
from parametric.ModifiedCovarianceMethod import ModifiedCovarianceMethod

sns.set()

def read_data(filename, delimiter, file_size):
    # Create reader
    data_file = open(filename)
    data_csv = csv.reader(data_file, delimiter=delimiter)

    # Init data
    x = np.zeros(file_size)
    file_column_count = file_size[1]

    # Read data
    row = 0
    for data_row in data_csv:
        for column in range(file_column_count):
            x[row][column] = data_row[column]
        row += 1
        
    return x

def plot_realisations(x, num=1):
    plt.figure()
    for i in range(num):
        plt.plot(x[i][:], label=i)
    plt.legend()
    plt.title('Data')
    plt.xlabel('t [s]')
    plt.show()

def apply_classical_methods(x):
    # Periodogram
    rand_index = randint(0, np.shape(x)[0])
    per = Periodogram()
    per.estimate(x[rand_index][:])
    per.plot()
    per.compare(x[rand_index][:])

    # Averaged periodogram
    rand_index = randint(0, np.shape(x)[0])
    avg_per = AveragedPeriodogram()
    avg_per.estimate(x[rand_index][:], L=50)
    avg_per.plot()
    avg_per.compare(x[rand_index][:], L=50)

    # Blackman-Tukey
    rand_index = randint(0, np.shape(x)[0])
    bm = BlackmanTukey()
    bm.estimate(x[rand_index][:], M=50)
    bm.plot()

def apply_parametric_methods(x):
    # Autocorrelaton method
    rand_index = randint(0, np.shape(x)[0])
    autocorr = AutocorrelationMethod()
    autocorr.estimate(x[rand_index][:], p=5)
    autocorr.plot()

    # Covariance method
    rand_index = randint(0, np.shape(x)[0])
    cov = CovarianceMethod()
    cov.estimate(x[rand_index][:], p=5)
    cov.plot()
    
    # Modified covariance method
    rand_index = randint(0, np.shape(x)[0])
    mod_cov = ModifiedCovarianceMethod()
    mod_cov.estimate(x[rand_index][:], p=5)
    mod_cov.plot()

    # Burg method
    # TODO

def window_closing_on_blackman_tukey(x):
    rand_index = randint(0, np.shape(x)[0])
    xr = x[rand_index][:]

    # Window closing and ploting
    bm = BlackmanTukey()
    plt.figure()
    for M in [10, 20, 40, 80, 160]:
        bm.estimate(xr, M=M)
        plt.semilogy(bm['f'], bm['P'], label=M)
    plt.title('Blackman-Tukey window closing')
    plt.legend()
    plt.xlabel('f [Hz]')
    plt.ylabel('P')
    plt.show()

def apply_and_plot_all(x):
    # Periodogram
    per = Periodogram()
    plt.figure()
    for i in range(np.shape(x)[0]):
        print('Estimating:', i)
        per.estimate(x[i][:])
        plt.semilogy(per['f'], per['P'])
    plt.title('Periodogram on all realisations')
    plt.xlabel('f [Hz]')
    plt.ylabel('P')
    plt.show()

    # CovarianceMethod
    cov = CovarianceMethod()
    plt.figure()
    for i in range(np.shape(x)[0]):
        print('Estimating:', i)
        cov.estimate(x[i][:], p=5)
        plt.semilogy(cov['f'], cov['P'])
    plt.title('Covariance method on all realisations')
    plt.xlabel('f [Hz]')
    plt.ylabel('P')
    plt.show()

    # Blackman-Tukey
    bm = BlackmanTukey()
    plt.figure()
    for i in range(np.shape(x)[0]):
        print('Estimating:', i)
        bm.estimate(x[i][:], M=10)
        plt.semilogy(bm['f'], bm['P'])
    plt.title('Blackman-Tukey on all realisations')
    plt.xlabel('f [Hz]')
    plt.ylabel('P')
    plt.show()

def apply_and_plot_with_order(x, p):
    cov = CovarianceMethod()
    
    for p_i in p:
        _, axarr = plt.subplots(1, 2)
        var = np.zeros(np.shape(x)[0])

        # Plot estimations for current p_i
        for i in range(np.shape(x)[0]):
            print('Estimating:', i)
            cov.estimate(x[i][:], p=p_i)

            axarr[0].semilogy(cov['f'], cov['P'])
            var[i] = cov['var_u']

        # Label subplots
        axarr[0].set_title('Covariance method for p = {}'.format(p_i))
        axarr[0].set(xlabel='f [Hz]', ylabel='P [dB]')

        axarr[1].stem(var)
        axarr[1].set_title('Variance for p = {}'.format(p_i))
        axarr[1].set(xlabel='realisation', ylabel='var')
        
        # Show current plot
        plt.show()

if __name__ == '__main__':
    # Read data
    x = read_data('data/data.csv', delimiter=',', file_size=[50, 256])
    #plot_realisations(x, num=2)

    # 1-2. Apply various methods for spectral estimation
    #apply_classical_methods(x)
    #apply_parametric_methods(x)

    # 3. Apply window closing and show results
    #window_closing_on_blackman_tukey(x)

    # 7. Apply a few methods on all realisations
    #apply_and_plot_all(x)

    # 9. Apply Covariance method with different orders.
    N = 256
    apply_and_plot_with_order(x, [N//2, N//4])
