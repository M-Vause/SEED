def example(input_data):
    from pySINDy.sindy import SINDy
    import numpy as np
    import csv
    
    data_path = './Data/' + input_data
    
    count = 0 #counter for row number
    variables = np.array([]) #array of variable names
    times = np.array([]) #time column of input data
    data = [] #data to use for the sindy model
    
    #code to create x & y values
    with open(data_path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            for value in range(len(row)):
                if count == 0:
                    variables = row
                elif count > 0:
                    if value == 0:
                        new_t = float(row[value])
                        times = np.append(times,new_t)
                        to_add = np.array([[float(row[1])]])
                    elif value > 1:
                        num = np.array([[float(row[value])]])
                        to_add = np.append(to_add,num,axis=0)
                    
            if count == 1:
                data = to_add
            elif count > 1:
                data = np.append(data,to_add,axis=1)
                    
            count = count + 1
            
    del variables[0]
    dt = times[1] - times[0]
  
    model = SINDy(name='SINDy model for Own Data')
    model.fit(data, dt, poly_degree=3, cut_off=0.01)
    coef = model.coefficients
    desc = model.descriptions

    return coef,desc