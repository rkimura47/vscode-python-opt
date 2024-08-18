from highspy import Highs, HighsModelStatus


def run_example():
    # TWT Problem Data
    jobs = tuple(i + 1 for i in range(4))
    jobPairs = [(i, j) for i in jobs for j in jobs if i < j]
    weight = dict(zip(jobs, (4, 5, 3, 5)))
    duration = dict(zip(jobs, (12, 8, 15, 9)))
    deadline = dict(zip(jobs, (16, 26, 27, 27)))
    M = sum(duration.values())

    # Create a new model
    model = Highs()

    # Create variables
    # x[(i,j)] = 1 if i << j, else j >> i
    x = {(i, j): model.addBinary(name=f"x[{i},{j}]") for i, j in jobPairs}
    startTime = {j: model.addVariable(name=f"startTime[{j}]") for j in jobs}
    tardiness = {j: model.addVariable(name=f"tardiness[{j}]") for j in jobs}

    # Add constraints
    for i, j in jobPairs:
        model.addConstr(
            startTime[j] >= startTime[i] + duration[i] - M * (1 - x[i, j]),
            name=f"NoOverlap1[{i},{j}]"
        )
        model.addConstr(
            startTime[i] >= startTime[j] + duration[j] - M * x[i, j],
            name=f"NoOverlap2[{i},{j}]"
        )

    for j in jobs:
        model.addConstr(
            tardiness[j] >= startTime[j] + duration[j] - deadline[j],
            name=f"Deadline[{j}]"
        )

    # AFAIK the only methods that allow setting the objective function
    # via linear expressions automatically calls model.run()
    model.minimize(sum(weight[j] * tardiness[j] for j in jobs))
    if model.getModelStatus() == HighsModelStatus.kUnboundedOrInfeasible:
        # Disable presolving to determine solve status
        model.setOptionValue("presolve", "off")
        model.clearSolver()
        model.run()

    model_status = model.getModelStatus()
    if model_status == HighsModelStatus.kOptimal:
        info = model.getInfo()
        sol = model.getSolution().col_value
        for var in model.getVariables():
            print("%s:\t%g" % (var.name, sol[var.index]))
        print("Objective:\t%g" % info.objective_function_value)
    else:
        print("Optimization was stopped with status %s" % model_status)
