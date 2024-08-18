import highspy


def run_example():
    # Initialize model object
    model = highspy.Highs()

    # Create variables
    x = model.addBinary(name="x")
    y = model.addBinary(name="y")
    z = model.addBinary(name="z")

    # Add constraints
    model.addConstr(x + 2 * y + 3 * z <= 4)
    model.addConstr(x + y >= 1)

    # Add objective function and solve
    model.maximize(x + y + 2 * z)

    # Print solutions
    info = model.getInfo()
    sol = model.getSolution().col_value
    print(f"Optimal objective value: {info.objective_function_value}")
    print(
        f"Solution values: x={sol[x.index]}, y={sol[y.index]}, z={sol[z.index]}"
    )
