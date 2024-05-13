import pyscipopt as scip


def run_example():
    # Initialize model object
    model = scip.Model()

    # Create variables
    x = model.addVar(vtype="B", name="x")
    y = model.addVar(vtype="B", name="y")
    z = model.addVar(vtype="B", name="z")

    # Add constraints
    model.addCons(x + 2 * y + 3 * z <= 4)
    model.addCons(x + y >= 1)

    # Add objective function
    model.setObjective(x + y + 2 * z, "maximize")

    # Solve it!
    model.optimize()

    # Print solutions
    print(f"Optimal objective value: {model.getObjVal()}")
    print(
        f"Solution values: x={model.getVal(x)}, y={model.getVal(y)}, z={model.getVal(z)}"
    )
