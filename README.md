# CES-Project

The optimisation_example_in_pyomo.py performs the following optimisation:
     
                                                      max x_1 + x_2
                                                           s.t.
                                                      x_1 + x_2 <= 1
                                                      x_2 <= 0.2*x_1

using pyomo, which is a collection of Python software packages for formulating optimization models. The solver "cplex" is used to solve the optimisation. 
