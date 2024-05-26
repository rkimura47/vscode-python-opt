from ortools.gscip.gscip_pb2 import GScipParameters
from ortools.math_opt.python import mathopt


def run_example():
    # TWT Problem Data
    jobs = tuple(i + 1 for i in range(4))
    jobPairs = [(i, j) for i in jobs for j in jobs if i < j]
    weight = dict(zip(jobs, (4, 5, 3, 5)))
    duration = dict(zip(jobs, (12, 8, 15, 9)))
    deadline = dict(zip(jobs, (16, 26, 25, 27)))
    M = sum(duration.values())

    # Create a new model
    model = mathopt.Model(name="TWTexample")

    # Create variables
    # x[(i,j)] = 1 if i << j, else j >> i
    x = {(i, j): model.add_binary_variable(name=f"x[{i},{j}]") for i, j in jobPairs}
    # Note: continuous variables in mathopt are NOT non-negative by default!
    startTime = {j: model.add_variable(lb=0.0, name=f"startTime[{j}]") for j in jobs}
    tardiness = {j: model.add_variable(lb=0.0, name=f"tardiness[{j}]") for j in jobs}

    # Set objective function
    model.minimize(mathopt.fast_sum(weight[j] * tardiness[j] for j in jobs))

    # Add constraints
    for i, j in jobPairs:
        model.add_linear_constraint(
            startTime[j] >= startTime[i] + duration[i] - M * (1 - x[i, j]),
            name=f"NoOverlap1[{i},{j}]",
        )
        model.add_linear_constraint(
            startTime[i] >= startTime[j] + duration[j] - M * x[i, j],
            name=f"NoOverlap2[{i},{j}]",
        )

    for j in jobs:
        model.add_linear_constraint(
            tardiness[j] >= startTime[j] + duration[j] - deadline[j],
            name=f"Deadline[{j}]",
        )

    # Solve model
    params = mathopt.SolveParameters(enable_output=True)
    result = mathopt.solve(model, mathopt.SolverType.GSCIP, params=params)
    if result.termination.reason == mathopt.TerminationReason.INFEASIBLE_OR_UNBOUNDED:
        # Disable presolving to determine solve status
        params = mathopt.SolveParameters(
            enable_output=True,
            gscip=GScipParameters(int_params={"presolving/maxrounds": 0}),
        )
        result = mathopt.solve(model, mathopt.SolverType.GSCIP, params=params)

    # Display solution
    if result.termination.reason == mathopt.TerminationReason.OPTIMAL:
        for var, val in result.variable_values().items():
            print("%s:\t%g" % (var.name, val))
        print("Objective:\t%g" % result.objective_value())
    else:
        term = result.termination
        print(
            "Optimization was stopped with status %s: %s"
            % (term.reason.name, term.detail)
        )
