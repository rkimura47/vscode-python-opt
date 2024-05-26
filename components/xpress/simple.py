import xpress as xp


def run_example():
    with xp.problem() as model:
        # Create variables
        x = model.addVariable(vartype=xp.binary, name="x")
        y = model.addVariable(vartype=xp.binary, name="y")
        z = model.addVariable(vartype=xp.binary, name="z")

        # Add constraints
        model.addConstraint(x + 2 * y + 3 * z <= 4)
        model.addConstraint(x + y >= 1)

        # Add objective function
        model.setObjective(x + y + 2 * z, sense=xp.maximize)

        # Solve it!
        model.mipoptimize()

        # Print solutions
        sol = model.getSolution({x: x, y: y, z: z})
        print(f"Optimal objective value: {model.getObjVal()}")
        print(f"Solution values: x={sol[x]}, y={sol[y]}, z={sol[z]}")
