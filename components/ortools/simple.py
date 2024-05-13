from ortools.math_opt.python import mathopt


def run_example():
    # Initialize model object
    model = mathopt.Model()

    # Create variables
    x = model.add_variable(lb=0.0, ub=1.0, is_integer=True, name="x")
    y = model.add_variable(lb=0.0, ub=1.0, is_integer=True, name="y")
    z = model.add_variable(lb=0.0, ub=1.0, is_integer=True, name="z")

    # Add constraints
    model.add_linear_constraint(x + 2 * y + 3 * z <= 4)
    model.add_linear_constraint(x + y >= 1)

    # Add objective function
    model.maximize(x + y + 2 * z)

    # Solve it!
    params = mathopt.SolveParameters(enable_output=True)
    result = mathopt.solve(model, mathopt.SolverType.GSCIP, params=params)
    # Print solutions
    sol = result.variable_values()
    print(f"Optimal objective value: {result.objective_value()}")
    print(f"Solution values: x={sol[x]}, y={sol[y]}, z={sol[z]}")
