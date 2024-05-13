import mip


def run_example():
    # Initialize environment and model objects
    model = mip.Model(solver_name=mip.CBC)

    # Create variables
    x = model.add_var(var_type=mip.BINARY, name="x")
    y = model.add_var(var_type=mip.BINARY, name="y")
    z = model.add_var(var_type=mip.BINARY, name="z")

    # Add constraints
    model.add_constr(x + 2 * y + 3 * z <= 4)
    model.add_constr(x + y >= 1)

    # Add objective function
    model.objective = mip.maximize(x + y + 2 * z)

    # Solve it!
    model.optimize()

    # Print solutions
    print(f"Optimal objective value: {model.objective_value}")
    print(f"Solution values: x={x.x}, y={y.x}, z={z.x}")
