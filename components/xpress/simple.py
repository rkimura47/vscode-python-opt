import xpress as xp


def run_example():
    with xp.problem() as model:
        # Create variables
        x = xp.var(vartype=xp.binary, name="x")
        y = xp.var(vartype=xp.binary, name="y")
        z = xp.var(vartype=xp.binary, name="z")
        model.addVariable(x, y, z)

        # Add constraints
        model.addConstraint(x + 2 * y + 3 * z <= 4)
        model.addConstraint(x + y >= 1)

        # Add objective function
        model.setObjective(x + y + 2 * z, sense=xp.maximize)

        # Solve it!
        model.solve()

        # Print solutions
        sol = model.getSolution({x: x, y: y, z: z})
        print(f"Optimal objective value: {model.getObjVal()}")
        print(f"Solution values: x={sol[x]}, y={sol[y]}, z={sol[z]}")
