function [vals,vars] = Own_Data(input_data)
    addpath('Data');
    addpath('Algorithms/sparsedynamics/examples/utils');

    %% read data
    data = readtable(input_data);
    vars = data.Properties.VariableNames;
    vars(1) = [];
    time = data(:,1);
    time = table2array(time);
    for d = 1:length(vars)
        x(:,d) = data(:,(d+1));
    end
    x = table2array(x);
    
    dt = time(2) - time(1);
    total_time = length(time)*dt;

    %% variables
    polyorder = 5;      % search space up to fifth order polynomials
    usesine = 0;        % no trig functions
    n = length(x(1,:)); % n-Dimensional system

    %%  Total Variation Regularized Differentiation
    for d = 1:n
        dxt(:,d) = TVRegDiff( x(:,d), 10, .00002, [], 'small', 1e12, dt, 1, 1 ); 
    end

    for d = 1:n
        xt(:,d) = cumsum(dxt(:,d))*dt;
    end
    
    for d = 1:n
        xt(:,d) = xt(:,d) - (mean(xt(1000:end-1000,d)) - mean(x(1000:end-1000,d)));
    end
    
    xt = xt(1000:end-1000,:);
    dxt = dxt(1000:end-1000,:);  % trim off ends (overly conservative)
    
    %% pool Data  (i.e., build library of nonlinear time series)
    Theta = poolData(xt,n,polyorder,usesine);
    m = size(Theta,2);
    
    %% compute Sparse regression: sequential least squares
    lambda = 0.02;      % lambda is our sparsification knob.
    Xi = sparsifyDynamics(Theta,dxt,lambda,n)
    vars = poolDataLIST(vars,Xi,n,polyorder,usesine);
    vals = Xi;
    
end