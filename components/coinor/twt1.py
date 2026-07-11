import mip


def run_example():
    # TWT Problem Data
    jobs = tuple(i + 1 for i in range(4))
    jobPairs = [(i, j) for i in jobs for j in jobs if i < j]
    weight = dict(zip(jobs, (4, 5, 3, 5), strict=True))
    duration = dict(zip(jobs, (12, 8, 15, 9), strict=True))
    deadline = dict(zip(jobs, (16, 26, 25, 27), strict=True))
    M = sum(duration.values())

    # Create a new model
    model = mip.Model(name="TWTexample", solver_name=mip.CBC)

    # Create variables
    # x[(i,j)] = 1 if i << j, else j >> i
    x = {
        (i, j): model.add_var(var_type=mip.BINARY, name=f"x[{i},{j}]")
        for i, j in jobPairs
    }
    startTime = {j: model.add_var(name=f"startTime[{j}]") for j in jobs}
    tardiness = {j: model.add_var(name=f"tardiness[{j}]") for j in jobs}

    # Set objective function
    model.objective = mip.minimize(
        mip.xsum(weight[j] * tardiness[j] for j in jobs)
    )

    # Add constraints
    for i, j in jobPairs:
        model.add_constr(
            startTime[j] >= startTime[i] + duration[i] - M * (1 - x[i, j]),
            name=f"NoOverlap1[{i},{j}]",
        )
        model.add_constr(
            startTime[i] >= startTime[j] + duration[j] - M * x[i, j],
            name=f"NoOverlap2[{i},{j}]",
        )

    for j in jobs:
        model.add_constr(
            tardiness[j] >= startTime[j] + duration[j] - deadline[j],
            name=f"Deadline[{j}]",
        )

    # Solve model
    status = model.optimize()

    # Display solution
    if status == mip.OptimizationStatus.OPTIMAL:
        for var in model.vars:
            print(f"{var.name}:\t{var.x:g}")
        print(f"Objective:\t{model.objective_value:g}")
    else:
        print(
            "Optimization was stopped with status "
            + f"{status.name} (code {status.value})"
        )
