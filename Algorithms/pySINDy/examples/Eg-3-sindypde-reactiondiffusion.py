def example():
    #import os
    #import sys
    #module_path = os.path.abspath(os.path.join('..'))
    #if module_path not in sys.path:
        #sys.path.append(module_path)

    from pySINDy.sindypde import SINDyPDE
    import scipy.io as sio
    import numpy as np

    # this .mat file can be generated from two of our .m files in datasets directory,
    # but since it's too large, we'll leave the user to generate the .mat file by themselves
    data = sio.loadmat('./Algorithms/pySINDy/datasets/reaction_diffusion.mat')
    #data.keys()
    print(data.keys())


    U = np.real(data['u'])
    V = np.real(data['v'])
    t = np.real(data['t'].flatten())
    x = np.real(data['x'].flatten())
    y = np.real(data['y'].flatten())
    dt = t[1] - t[0]
    dx = x[1] - x[0]
    dy = y[1] - y[0]
    

    model = SINDyPDE(name='SINDyPDE model for Reaction-Diffusion Eqn')


    U1 = U[100:200, 100:200, 200:230]
    V1 = V[100:200, 100:200, 200:230]
    model.fit({'u': U1, 'v': V1}, dt, [dx, dy], space_deriv_order=2, poly_degree=2, sample_rate=0.01, cut_off=0.05, deriv_acc=5)


    activated1 = [model.descriptions[i] for i in np.arange(model.coefficients.shape[0]) if model.coefficients[i, 0] != 0]
    activated2 = [model.descriptions[i] for i in np.arange(model.coefficients.shape[0]) if model.coefficients[i, 1] != 0]

    #print(activated1)
    #print(activated2)

    x = model.coefficients
    y = model.descriptions
    
    return x,y

    from findiff import FinDiff
    deriv_acc = 5

    U1 = U[100:200, 100:200, 200:230]
    V1 = V[100:200, 100:200, 200:230]

    d1_dt = FinDiff(U1.ndim-1, dt, 1, acc=deriv_acc)
    d2_xx = FinDiff(0, dx, 2, acc=deriv_acc)
    d2_yy = FinDiff(1, dy, 2, acc=deriv_acc)

    u_t = d1_dt(U1).flatten()
    v_t = d1_dt(V1).flatten()
    x_t = np.vstack([u_t, v_t]).T
    print('finished time derivative computation!')

    u_xx = d2_xx(U1).flatten()
    u_yy = d2_yy(U1).flatten()
    v_xx = d2_xx(V1).flatten()
    v_yy = d2_yy(V1).flatten()
    u = U1.flatten()
    v = V1.flatten()
    uv2 = (U1*V1*V1).flatten()
    u2v = (U1*U1*V1).flatten()
    u3 = (U1*U1*U1).flatten()
    v3 = (V1*V1*V1).flatten()

    lib = np.vstack([u_xx, u_yy, v_xx, v_yy, u, v, uv2, u2v, u3, v3]).T

    print(np.linalg.lstsq(lib, x_t, rcond=None)[0])
    


def get_params():
    variables = ["dt", "dx", "dy"]
    values = [0.01, 0.01953125, 0.01953125]
    return variables,values
