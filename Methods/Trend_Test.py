'''
Trend Test

    by King Lee 2022.10.6

    From this method, you can do the trend test and obtain the basic statistical magnitudes, like slope, p_value, r_value and etc. I 
    provide 2 methods, one is linear regression (based on Linear least squares regression), and another one is Mann_Kendall_Test.
    
    What's more, if you need to do batch computing, so you would like to use function_region_trend_test, which will use all the core
    your machine has to help you accelerate the computing process.

    Also, if needed, I'll keep updating other trend test methods.
'''
#%% trend test

import scipy.stats as stats
import pymannkendall as mk
import numpy as np


def linreg(x, y):
    '''
    linear regression (based on Linear least squares regression)
    :param x:
    :param y:
    :return:
            slope, r_value, p_value
    '''
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    return slope, r_value, p_value


def mk_test(y):
    '''
    Mann_Kendall_Test
    :param y: a sequence 
    
    :return : (trend='increasing', h=True, p=3.019806626980426e-14, z=7.597015044026804, Tau=1.0, s=406.0, var_s=2842.0, slope=1.0, intercept=1992.0)
                here output the p(MK_test[2]) and Tau(MK_test[4])
    
    '''
    
    MK_test = mk.original_test(y)

    return MK_test[2], MK_test[4]


#%% regional trend test
import multiprocessing as mp

def region_trend_test(var, x_len, y_len):
    '''
    Regional trend test(use multiprocessing to accelerate the calculation)

    :param var: 3D-array, which includes:(time, x, y)
    :x_len: the length of x-axis
    :y_len: the length of y-axis

    '''

    cores = mp.cpu_count()
    pool = mp.Pool(processes=cores)
    
    multi_res = []
    
    for x in np.arange(x_len):
        print(x)
    
        multi_res.append([pool.apply_async(linreg, (np.arange(var.shape[0]), var[:, x, y],)) for y in np.arange(y_len)])


    grid_trend = np.zeros([3, x_len, y_len])

    for x in np.arange(x_len):
        print(x)

        for y in np.arange(y_len):

            grid_trend[:, x, y] = np.array(multi_res[x][y].get())
    
    return grid_trend