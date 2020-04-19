function [vals,vars] = test_eg_ml(varargin)
	if nargin==0 % There are no input arguments
        [vals,vars] = run();
    else % There is an input argument
        [vals,vars] = get_params();
    end
end

function [vals,vars] = run()
    vals = [1 -1; 0.3 -0.3; 0.3 -0.3; 1 -1; 0.01 -0.01; 1 -1];
    vars = ["var1" "var2" "var3" "var4" "var5" "var6"];
end

function [variables,values] = get_params()
    variables = {'a', 'b', 'c', 'd'};
    values = {3.14, '0.1; 5.0',0.005, '0.0; 25.0'};
end