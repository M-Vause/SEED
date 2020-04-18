def example():
    #import os
    #import sys
    #module_path = os.path.abspath(os.path.join('..'))
    #module_path = module_path + "/Final/Algorithms/pySINDy"
    #if module_path not in sys.path:
        #sys.path.append(module_path)
    
    from pySINDy.sindypde import SINDyPDE
    import scipy.io as sio
    import numpy as np
    
    #data = sio.loadmat('../datasets/burgers.mat')
    data = sio.loadmat('../SEED/Algorithms/pySINDy/datasets/burgers.mat')
    data.keys()
    
    U = np.real(data['usol'])
    t = np.real(data['t'].flatten())
    x = np.real(data['x'].flatten())
    dt = t[1] - t[0]
    dx = x[1] - x[0]
    
    model = SINDyPDE(name='SINDyPDE model for Burgers')
    
    model.fit(U, dt, dx, space_deriv_order=2, cut_off=0.1)
    
    x = model.coefficients
    y = model.descriptions
    #model.plot_coefficients
    
    return x,y
    
def get_params():
    variables = ["dt", "dx"]
    values = [0.1, 0.0625]
    return variables,values
