import cplex._internal._constants as CPLEX_CONSTANTS
from docplex.mp.model import Model

# See "Solution Status Codes by Number in the CPLEX Callable Library (C API)" in the CPLEX documentation
# https://www.ibm.com/docs/en/icos/22.1.1?topic=micclcarm-solution-status-codes-by-number-in-cplex-callable-library-c-api
StatusDict = {
    getattr(CPLEX_CONSTANTS, c): c
    for c in dir(CPLEX_CONSTANTS)
    if c.isupper() and (c.startswith("CPX_STAT") or c.startswith("CPXMIP"))
}
INF_OR_UNBD_STATUS = [
    CPLEX_CONSTANTS.CPX_STAT_INForUNBD,
    CPLEX_CONSTANTS.CPXMIP_INForUNBD,
    CPLEX_CONSTANTS.CPX_STAT_MULTIOBJ_INForUNBD,
]


def run_example():
    # TWT Problem Data
    jobs = tuple([i + 1 for i in range(4)])
    jobPairs = [(i, j) for i in jobs for j in jobs if i < j]
    weight = dict(zip(jobs, (4, 5, 3, 5)))
    duration = dict(zip(jobs, (12, 8, 15, 9)))
    deadline = dict(zip(jobs, (16, 26, 25, 27)))
    M = sum(duration.values())

    # Create a new model
    with Model(name="TWTexample", log_output=True) as m:
        # Create variables
        # x_i_j = 1 if i << j, else j >> i
        x = m.binary_var_dict(jobPairs, name="x")
        startTime = m.continuous_var_dict(jobs, name="startTime")
        tardiness = m.continuous_var_dict(jobs, name="tardiness")

        # Set objective function
        m.minimize(m.sum(weight[j] * tardiness[j] for j in jobs))

        # Add constraints
        m.add_constraints(
            (
                startTime[j] >= startTime[i] + duration[i] - M * (1 - x[(i, j)]),
                "NoOverlap1_%d_%d" % (i, j),
            )
            for (i, j) in jobPairs
        )
        m.add_constraints(
            (
                startTime[i] >= startTime[j] + duration[j] - M * x[(i, j)],
                "NoOverlap2_%d_%d" % (i, j),
            )
            for (i, j) in jobPairs
        )
        m.add_constraints(
            (
                tardiness[j] >= startTime[j] + duration[j] - deadline[j],
                "Deadline_%d" % j,
            )
            for j in jobs
        )

        # Solve model
        solve_solution = m.solve()

        if m.solve_details.status_code in INF_OR_UNBD_STATUS:
            # Disable primal/dual reductions to determine solve status
            m.parameters.preprocessing.reduce = False
            m.solve()

        # Display solution
        if solve_solution:
            for v in m.iter_variables():
                print("%s:\t%g" % (v.name, v.solution_value))
            print("Objective:\t%g" % m.objective_value)
        else:
            sdetails = m.solve_details
            print(
                "Optimization was stopped with status: %s (code %d)"
                % (sdetails.status, sdetails.status_code)
            )
