# CES-Project

The optimisation_example_in_pyomo.py performs the following optimisation:
     
                                                      max x1 + x2
                                                           s.t.
                                                      x1 + x2 <= 1
                                                      x2 <= 0.2*x1
                                                      x1 , x2 >= 0

using pyomo, which is a collection of Python software packages for formulating optimization models. The solver "cplex" is used to solve the optimisation. 
