from ortools.math_opt.python import mathopt


def run_example(L: int, n: int):
    """Run Golomb ruler example.

    Args:
        L: Length of ruler
        n: Number of marks
    """
    model = mathopt.Model()

    marks = range(L + 1)
    mark_pairs = [(i, j) for i in marks for j in marks if i < j]
    # x_i = 1 if mark i is chosen, 0 otherwise
    x = {m: model.add_binary_variable(name=f"x[{m}]") for m in marks}
    # y_ij = 1 iff x_i = 1 AND x_k = 1
    y = {pair: model.add_binary_variable(name=f"y[{pair[0]},{pair[1]}]") for pair in mark_pairs}

    # Among all possible pairs of marks measuring length k, there can be at most 1.
    for k in range(1, L):
        model.add_linear_constraint(
            mathopt.fast_sum(y[i, i + k] for i in range(L - k + 1)) <= 1,
            name=f"UniqueLength[{k}]"
        )

    # Enforce y_ij == x_i AND x_k
    # For this problem we can get away with only enforcing
    # (x_i = 1 AND x_j = 1) -> y_ij = 1
    for (i, j), y_var in y.items():
        model.add_linear_constraint(x[i] + x[j] - 1 <= y_var)

    # Either require at least n marks, or try to maximize the number of marks.
    model.add_linear_constraint(mathopt.fast_sum(x.values()) >= n, name="RequireNMarks")
    # model.maximize(mathopt.fast_sum(x.values()))

    # We can use either CP-SAT or SCIP; unsurprisingly, CP-SAT is generally faster for this problem.
    params = mathopt.SolveParameters(enable_output=True)
    result = mathopt.solve(model, mathopt.SolverType.CP_SAT, params=params)
    # result = mathopt.solve(model, mathopt.SolverType.GSCIP, params=params)

    if result.has_primal_feasible_solution():
        print("## Golomb Ruler Problem ##")
        print(f"L = {L}, n = {n}")
        sol = result.variable_values()
        used_marks = [idx for idx, var in x.items() if sol[var] > 0]
        print(f"used_marks = {used_marks}")