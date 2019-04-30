import numpy as np
from scipy import signal
from parametric.Autocorrelation import Autocorrelation
from parametric.AutocorrelationMethod import AutocorrelationMethod
from parametric.CovarianceMethod import CovarianceMethod

def autocorrelation_method_test():
    t = np.arange(1000)
    x = np.sin(1*t + 2.8) + np.sin(2*t + 3.4)
    autocorr_method = AutocorrelationMethod()

    # Estimation
    autocorr_method.estimate(x, p=4)
    autocorr_method.plot()

def autocorrelation_test():
    x = np.random.normal(size=1000)
    r_xx = Autocorrelation()

    # Estimation
    r_xx.estimate(x)
    r_xx.plot()

    # Comparation
    r_xx.compare(x)

def covariance_method_test():
    t = np.arange(1000)
    x = np.sin(1*t + 2.8) + np.sin(2*t + 3.4)
    #x = np.random.normal(size=1000)
    cov_method = CovarianceMethod()

    # Estimation
    cov_method.estimate(x, p=4)
    cov_method.plot()

    print('var_u: ', cov_method['var_u'])

if __name__ == "__main__":
    #autocorrelation_test()
    #autocorrelation_method_test()
    covariance_method_test()