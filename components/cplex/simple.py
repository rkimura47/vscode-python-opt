from docplex.mp.model import Model


def run_example():
    with Model() as model:
        # Create variables
        x = model.binary_var(name="x")
        y = model.binary_var(name="y")
        z = model.binary_var(name="z")

        # Add constraints
        model.add_constraint(x + 2 * y + 3 * z <= 4)
        model.add_constraint(x + y >= 1)

        # Add objective function
        model.maximize(x + y + 2 * z)

        # Solve it!
        model.solve(log_output=True)

        # Print solutions
        print(f"Optimal objective value: {model.objective_value}")
        print(
            f"Solution values: x={x.solution_value}, y={y.solution_value}, z={z.solution_value}"
        )
