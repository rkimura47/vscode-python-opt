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
    jobs = tuple(i + 1 for i in range(4))
    jobPairs = [(i, j) for i in jobs for j in jobs if i < j]
    weight = dict(zip(jobs, (4, 5, 3, 5), strict=True))
    duration = dict(zip(jobs, (12, 8, 15, 9), strict=True))
    deadline = dict(zip(jobs, (16, 26, 25, 27), strict=True))
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
                startTime[j] >= startTime[i] + duration[i] - M * (1 - x[i, j]),
                f"NoOverlap1_{i}_{j}",
            )
            for i, j in jobPairs
        )
        m.add_constraints(
            (
                startTime[i] >= startTime[j] + duration[j] - M * x[i, j],
                f"NoOverlap2_{i}_{j}",
            )
            for i, j in jobPairs
        )
        m.add_constraints(
            (
                tardiness[j] >= startTime[j] + duration[j] - deadline[j],
                f"Deadline_{j}",
            )
            for j in jobs
        )

        # Solve model
        solve_solution = m.solve()

        if m.solve_details.status_code in INF_OR_UNBD_STATUS:
            # Disable primal/dual reductions to determine solve status
            m.parameters.preprocessing.reduce = False
            solve_solution = m.solve()

        # Display solution
        if solve_solution:
            for v in m.iter_variables():
                print(f"{v.name}:\t{v.solution_value:g}")
            print(f"Objective:\t{m.objective_value:g}")
        else:
            sdetails = m.solve_details
            print(
                "Optimization was stopped with status: "
                + f"{sdetails.status} (code {sdetails.status_code})"
            )
