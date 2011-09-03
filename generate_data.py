#    numerical python
import numpy as np


def generate_data( m, s, n):
    #    check means and sigmas are same length
    if len(m) != len(s):
        print('means and sigmas must be same length') 
        return
       
    #   generate normally distributed matrix
    R = np.random.standard_normal(size = (n, len(s)))
    
    #    adjust to requested means and sigmas
    R = np.tile(m, (n, 1)) + np.tile(s, (n, 1)) * R
    
    return R
