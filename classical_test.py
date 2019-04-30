import numpy as np
from classical.Periodogram import Periodogram
from classical.AveragedPeriodogram import AveragedPeriodogram
from classical.Autocorrelation import Autocorrelation
from classical.BlackmanTukey import BlackmanTukey
from classical.BlackmanTukey import TriangWindow

def periodogram_test():
    t = np.arange(256)
    x = np.sin(1*t + 2.8) + np.sin(2*t + 3.4)
    per = Periodogram()

    # Estimation
    per.estimate(x)
    per.plot()

    # Comparation
    per.compare(x)

def averaged_periodogram_test():
    t = np.arange(256)
    x = np.sin(1*t + 2.8) + np.sin(2*t + 3.4)
    per = AveragedPeriodogram()

    # Estimation
    per.estimate(x, L=100)
    per.plot()

    # Comparation
    per.compare(x, 100)

def autocorrelation_test():
    x = np.random.normal(size=1000)
    r_xx = Autocorrelation()

    # Estimation
    r_xx.estimate(x)
    r_xx.plot()

    # Comparation
    r_xx.compare(x)

def blackmantukey_test():
    t = np.arange(256)
    x = np.sin(1*t + 2.8) + np.sin(2*t + 3.4)
    bm = BlackmanTukey()

    # Estimation
    bm.estimate(x)
    bm.plot()

if __name__ == "__main__":
    #periodogram_test()
    #averaged_periodogram_test()
    #autocorrelation_test()
    blackmantukey_test()