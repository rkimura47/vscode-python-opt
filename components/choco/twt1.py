from pychoco import Model

def run_example():
    # TWT Problem Data
    jobs = tuple(i + 1 for i in range(4))
    weight = dict(zip(jobs, (4, 5, 3, 5)))
    duration = dict(zip(jobs, (12, 8, 15, 9)))
    deadline = dict(zip(jobs, (16, 26, 25, 27)))
    MAX_END_TIME = sum(duration.values())
    UB_TWT = MAX_END_TIME * sum(weight.values())

    # Create a new model
    model = Model("TWTexample")

    # Create variables
    startTime = {j: model.intvar(0, MAX_END_TIME, name=f"startTime[{j}]") for j in jobs}
    tardiness = {j: model.intvar(0, MAX_END_TIME, name=f"tardiness[{j}]") for j in jobs}
    # Auxiliary variables
    endTime = {j: model.intvar(0, MAX_END_TIME, name=f"endTime[{j}]") for j in jobs}
    tasks = [model.task(startTime[j], duration[j], endTime[j]) for j in jobs]
    heights = [model.intvar(1) for _ in jobs]
    capacity = model.intvar(1)

    # Add constraints
    model.cumulative(tasks, heights, capacity).post()
    for j in jobs:
        model.arithm(endTime[j], "-", deadline[j], "<=", tardiness[j]).post()

    # Add objective function
    obj_twt = model.intvar(0, UB_TWT, name="obj_twt")
    model.scalar([tardiness[j] for j in jobs], [weight[j] for j in jobs], "<=", obj_twt).post()

    # Solve model
    solver = model.get_solver()
    solver.show_short_statistics()
    solution = solver.find_optimal_solution(objective=obj_twt, maximize=False)


    # Display solution
    if solution:
        for var in startTime.values():
            print("%s:\t%g" % (var.name, solution.get_int_val(var)))
        for var in tardiness.values():
            print("%s:\t%g" % (var.name, solution.get_int_val(var)))

        print("Objective:\t%g" % solution.get_int_val(obj_twt))
    else:
        status = solver.get_search_state()
        is_optimal = solver.is_objective_optimal() == 1
        num_solutions = solver.get_solution_count()
        print(
            f"Optimization was stopped with status {status}: "
            + f"{num_solutions} solutions, is_optimal = {is_optimal}"
        )
