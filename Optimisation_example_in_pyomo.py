# Required libraries and packages
from pyomo.environ import NonNegativeReals
from pyomo.environ import ConstraintList
from pyomo.environ import ConcreteModel
from pyomo.environ import Var
from pyomo.environ import Objective
from pyomo.opt import SolverFactory


# Create a concrete model
model = ConcreteModel()

# Define Optimisation Variables x1 and x2
model.x = Var(range(1, 3), within=NonNegativeReals)

# Define Optimisation Constraints :
model.Const = ConstraintList()

model.Const.add(model.x[1] + model.x[2] <= 1)
model.Const.add(0.2 * model.x[1] - model.x[2] <= 0)


# Define Objective Function
def Objrule(model):

    return -(model.x[1] + model.x[2])


model.obj = Objective(rule=Objrule)

# Solve the Optimisation Model
opt = SolverFactory("cplex")
results = opt.solve(model)

# Results
print("x1 is ", model.x[1].value)
print("x2 is ", model.x[2].value)
