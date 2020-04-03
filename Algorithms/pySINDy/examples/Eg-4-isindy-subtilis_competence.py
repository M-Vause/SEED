def example():
    #import os
    #import sys
    #module_path = os.path.abspath(os.path.join('..'))
    #if module_path not in sys.path:
        #sys.path.append(module_path)

    import numpy as np
    import scipy as sp
    import scipy.integrate as integrate
    import matplotlib.pyplot as plt
    from pySINDy.sindypde import SINDyPDE
    from pySINDy.isindy import ISINDy

    def subtilis_competence(t,S):
        S_1 = S[0]
        S_2 = S[1]

        a1 = 0.004
        a2 = 0.07
        a3 = 0.04
        b1 = 0.82
        b2 = 1854.5


        v1 = (a2*S_1**2)/(a3+S_1**2)
        v2 = b1/(1+b2*S_1**5)
        v3 = S_1/(1+S_1+S_2)
        v4 = S_2/(1+S_1+S_2)
    
        return [a1 + v1 - v3, v2 - v4]

    n = 2
    dt = 0.001
    tspan = np.arange(0, 5 + dt, dt)
    len_t = len(tspan)
    np.random.seed(0)
    sinit = np.random.rand(n)
    sol = integrate.solve_ivp(subtilis_competence, [0, len_t], sinit, t_eval=tspan, rtol = 1e-7, atol = 1e-7)

    xt = sol.y

    isindy_model = ISINDy(name = 'isindy')
    data = isindy_model.fit(xt, 0.001, poly_degree=5)

    x = isindy_model.coefficients

    y = isindy_model.descriptions

    #isindy_model.plot_coefficients

    return x,y

def get_params():
    variables = ["n", "dt", "Timespan"]
    values = [2.0, 0.001, [0.0, 5.0]]
    return variables,values
