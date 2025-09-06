import xpress as xp
from xpress.enums import MIPStatus

MipStatusDict = {getattr(xp, s): s for s in dir(xp) if s.startswith("mip")}


def run_example():
    # TWT Problem Data
    jobs = tuple(i + 1 for i in range(4))
    jobPairs = [(i, j) for i in jobs for j in jobs if i < j]
    weight = dict(zip(jobs, (4, 5, 3, 5)))
    duration = dict(zip(jobs, (12, 8, 15, 9)))
    deadline = dict(zip(jobs, (16, 26, 25, 27)))
    M = sum(duration.values())

    # Create a new model
    m = xp.problem("TWTexample")

    # Create variables
    # x[(i,j)] = 1 if i << j, else j >> i
    x = m.addVariables(jobPairs, vartype=xp.binary, name="x")
    startTime = m.addVariables(jobs, name="startTime")
    tardiness = m.addVariables(jobs, name="tardiness")

    # Set objective function
    m.setObjective(xp.Sum(weight[j] * tardiness[j] for j in jobs), sense=xp.minimize)

    # Add constraints
    m.addConstraint(
        xp.constraint(
            startTime[j] >= startTime[i] + duration[i] - M * (1 - x[i, j]),
            name=f"NoOverlap1[{i},{j}]",
        )
        for i, j in jobPairs
    )
    m.addConstraint(
        xp.constraint(
            startTime[i] >= startTime[j] + duration[j] - M * x[i, j],
            name=f"NoOverlap2[{i},{j}]",
        )
        for i, j in jobPairs
    )
    m.addConstraint(
        xp.constraint(
            tardiness[j] >= startTime[j] + duration[j] - deadline[j],
            name=f"Deadline[{j}]",
        )
        for j in jobs
    )

    # Solve model
    m.mipoptimize()

    # Display solution
    if m.attributes.mipstatus == MIPStatus.OPTIMAL:
        solution = m.getSolution({v: v for v in m.getVariable()})
        for var, val in solution.items():
            print("%s:\t%g" % (var.name, val))
        print("Objective:\t%g" % m.attributes.objval)
    else:
        mipstatus = m.attributes.mipstatus
        print(
            "Optimization was stopped with status: %s (MIPSTATUS=%d)"
            % (MipStatusDict[mipstatus], mipstatus)
        )
