% Copyright 2015, All Rights Reserved
% Code by Steven L. Brunton
% For Paper, "Discovering Governing Equations from Data: 
%        Sparse Identification of Nonlinear Dynamical Systems"
% by S. L. Brunton, J. L. Proctor, and J. N. Kutz

function [vals,vars] = EX04a_LogisticMap(varargin)
	if nargin==0 % There are no input arguments
        [vals,vars] = run();
    else % There is an input argument
        [vals,vars] = get_params();
    end
end

function [vals,vars] = run()
    clear all, close all, clc
    figpath = '../figures/';
    %addpath('./utils');
    addpath('Algorithms/sparsedynamics/examples/utils');

    % generate Data
    N = 1000;
    eps = 0.01; % eps = 0.025;
    x = [];
    dx = [];
    for r = [2.5 2.75 3 3.25 3.5 3.75 3.8 3.85 3.9 3.95];
        xt(1,1) = .5;  % initial condition
        xt(1,2) = r;
        for k=2:N;
            xt(k,1) = r*xt(k-1,1)*(1-xt(k-1,1)) + eps*randn;
            xt(k,1) = min(xt(k,1),1);
            xt(k,1) = max(xt(k,1),0);
            xt(k,2) = r;
        end
        x = [x; xt(1:end-1,:)];
        dx = [dx; xt(2:end,:)];
    end
    %% pool Data
    Theta = poolData(x,2,5,0);
    m = size(Theta,2);

    Xi = Theta\dx;
    XiB = Xi;
    % iterative least squares solution
    for k=1:5
        posinds = find(abs(Xi)<.5);  
        Xi(posinds)=0;
        XiC = Xi;
        for ind = 1:2
            Xitemp = Xi(:,ind);
            posinds = find(abs(Xitemp)>=.5)
            Xi(posinds,ind) = Theta(:,posinds)\dx(:,ind);
        end
        XiD = Xi;
    end
    norm(Theta*XiD - dx)/norm(dx)

    %% Noisy data full
    xvals=[];
    startval = 1;
    endval = 4;
    for r=startval:.0005:endval
        r
        xold = 0.5;
        for i=1:1000
            xnew = r*xold - r*xold^2 + eps*randn;
            xnew = min(xnew,1);
            xnew = max(xnew,0);           
            xold = xnew;
        end
        xss = xnew;
        for i=1:1000               
            xnew = r*xold - r*xold^2 + eps*randn;
            xnew = min(xnew,1);
            xnew = max(xnew,0);           
            xold = xnew;
            xvals(2,length(xvals)+1) = r;
            xvals(1,length(xvals)) = xnew;
            if(abs(xnew-xss)<.001)
                break
            end
        end   
    end

    figure
    rr=axes('Position',[0 0 1 1]);
    plot(rr,xvals(1,:),xvals(2,:),'.','LineWidth',.2,'MarkerSize',2,'Color',[0 0 0])
    hold on
    plot(rr,x(:,1),x(:,2),'.','LineWidth',1,'MarkerSize',5,'Color',[1 0 0])
    axis([0 1 startval endval])
    set(gca,'YDir','reverse');

    %% Recon full
    figure
    rr=axes('Position',[0 0 1 1]);
    xvals=[];
    startval = 1;
    endval = 4;

        a1 = Xi(5,1);
        a2 = Xi(8,1);
    for r=startval:.0005:endval
        r
        xold = 0.5;
        for i=1:1000
            xnew = r*a1*xold + r*a2*xold^2;             
            xold = xnew;
        end
        xss = xnew;
        for i=1:1000               
            xnew = r*a1*xold + r*a2*xold^2;             
            xold = xnew;
            xvals(2,length(xvals)+1) = r;
            xvals(1,length(xvals)) = xnew;
            if(abs(xnew-xss)<.001)
                break
            end
        end

    end
    plot(rr,xvals(1,:),xvals(2,:),'.','LineWidth',.2,'MarkerSize',2,'Color',[0 0 0])
    axis([0 1 startval endval])
    set(gca,'YDir','reverse');
    
%     vars = poolDataLIST({'x','y','z'},Xi,M,polyorder,usesine);
%     vals = Xi;
    vars = {'0'};%cell(1);
    vals = [0 0];
end

function [variables,values] = get_params()
    variables = {};
    values = {};
end