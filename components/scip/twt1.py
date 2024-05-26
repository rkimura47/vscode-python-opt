from pyscipopt import Model, quicksum


def run_example():
    # TWT Problem Data
    jobs = tuple(i + 1 for i in range(4))
    jobPairs = [(i, j) for i in jobs for j in jobs if i < j]
    weight = dict(zip(jobs, (4, 5, 3, 5)))
    duration = dict(zip(jobs, (12, 8, 15, 9)))
    deadline = dict(zip(jobs, (16, 26, 25, 27)))
    M = sum(duration.values())

    # Create a new model
    model = Model("TWTexample")

    # Create variables
    # x[(i,j)] = 1 if i << j, else j >> i
    x = {(i, j): model.addVar(vtype="B", name=f"x[{i},{j}]") for i, j in jobPairs}
    startTime = {j: model.addVar(name=f"startTime[{j}]") for j in jobs}
    tardiness = {j: model.addVar(name=f"tardiness[{j}]") for j in jobs}

    # Set objective function
    model.setObjective(quicksum([weight[j] * tardiness[j] for j in jobs]), "minimize")

    # Add constraints
    model.addConss(
        (
            startTime[j] >= startTime[i] + duration[i] - M * (1 - x[i, j])
            for i, j in jobPairs
        ),
        "NoOverlap1",
    )
    model.addConss(
        (startTime[i] >= startTime[j] + duration[j] - M * x[i, j] for i, j in jobPairs),
        "NoOverlap2",
    )
    model.addConss(
        (tardiness[j] >= startTime[j] + duration[j] - deadline[j] for j in jobs),
        "Deadline",
    )

    # Solve model
    model.optimize()
    if model.getStatus() == "inforunbd":
        # Disable presolving to determine solve status
        model.setParams({"presolving/maxrounds": 0})
        model.freeTransform()
        model.optimize()

    # Display solution
    status = model.getStatus()
    if status == "optimal":
        for v in model.getVars():
            print("%s:\t%g" % (v.name, model.getVal(v)))
        print("Objective:\t%g" % model.getObjVal())
    else:
        print("Optimization was stopped with status %s" % status)
