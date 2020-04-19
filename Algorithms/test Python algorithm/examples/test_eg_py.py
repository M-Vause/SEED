def example():
    import numpy as np
    
    print("Successful Python test")
  
    # Say HI
    coef = np.array([[1, -1],[0.3, -0.3],[0.3, -0.3],[1,-1],[0.01,-0.01],[1,-1]])
    desc = ["var1", "var2", "var3", "var4","var5","var6"]

    return coef,desc

def get_params():
    variables = ["a", "b", "c", "d"]
    values = [3.14, [0.1, 5.0], 0.005, [0.0, 10.0]]
    return variables,values