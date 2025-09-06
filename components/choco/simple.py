from pychoco import Model

def run_example() -> None:
    # Initialize model object
    model = Model()

    # Create variables
    # Note: pychoco does not support continuous variables
    x = model.intvar(0, 1, name="x")
    y = model.intvar(0, 1, name="y")
    z = model.intvar(0, 1, name="z")

    # Add constraints
    model.scalar([x, y, z], [1, 2, 3], "<=", 4).post()
    model.sum([x, y], ">=", 1).post()

    # Add objective function
    # Thankfully we have decent bounds on the objective value
    obj = model.intvar(0, 4, name="obj")
    model.scalar([x, y, z], [1, 1, 2], "=", obj).post()

    # Solve it!
    solver = model.get_solver()
    solver.show_short_statistics()
    sol = solver.find_optimal_solution(objective=obj, maximize=True)

    # Print solutions
    print(f"Optimal objective value: {sol.get_int_val(obj)}")
    print(
        f"Solution values: x={sol.get_int_val(x)}, y={sol.get_int_val(y)}, z={sol.get_int_val(z)}"
    )
