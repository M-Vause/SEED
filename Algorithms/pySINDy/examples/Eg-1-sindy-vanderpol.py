def example():
    #import os
    #import sys
    #module_path = os.path.abspath(os.path.join('..'))
    #module_path = module_path + "/Final/Algorithms/pySINDy"
    #if module_path not in sys.path:
        #sys.path.append(module_path)
    
    from pySINDy.sindy import SINDy
    import numpy as np
    import matplotlib.pyplot as plt
    from pySINDy.utils.generator import van_der_pol_generator

    mu = 1.2
    xinit = [0.1, 5.0]
    dt = 0.01
    len_t = 100

    data = van_der_pol_generator(mu, xinit, dt, len_t)

    model = SINDy(name='my_sindy_model')
    model.fit(data, dt, poly_degree=3, cut_off=0.01)
    x=model.coefficients
    y=model.descriptions
    #model.plot_coefficients

    return x,y

def get_params():
    variables = ["mu", "Initial Conditions", "dt", "Timespan"]
    values = [1.2, [0.1, 5.0], 0.01, [0.0, 100.0]]
    return variables,values