import gurobipy as grb


def run_example():
    # Initialize environment and model objects
    with grb.Env() as env, grb.Model(env=env) as model:
        # Create variables
        x = model.addVar(vtype=grb.GRB.BINARY, name="x")
        y = model.addVar(vtype=grb.GRB.BINARY, name="y")
        z = model.addVar(vtype=grb.GRB.BINARY, name="z")

        # Add constraints
        model.addConstr(x + 2 * y + 3 * z <= 4)
        model.addConstr(x + y >= 1)

        # Add objective function
        model.setObjective(x + y + 2 * z, grb.GRB.MAXIMIZE)

        # Solve it!
        model.optimize()

        # Print solutions
        print(f"Optimal objective value: {model.ObjVal}")
        print(f"Solution values: x={x.X}, y={y.X}, z={z.X}")
