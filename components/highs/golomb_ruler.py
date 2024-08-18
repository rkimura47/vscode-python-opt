from highspy import Highs, SolutionStatus


def run_example(L: int, n: int):
    """Run Golomb ruler example.

    Args:
        L: Length of ruler
        n: Number of marks
    """
    model = Highs()

    marks = range(L + 1)
    mark_pairs = [(i, j) for i in marks for j in marks if i < j]
    # x_i = 1 if mark i is chosen, 0 otherwise
    x = {m: model.addBinary(name=f"x[{m}]") for m in marks}
    # y_ij = 1 iff x_i = 1 AND x_k = 1
    y = {
        pair: model.addBinary(name=f"y[{pair[0]},{pair[1]}]")
        for pair in mark_pairs
    }

    # Among all possible pairs of marks measuring length k, there can be at most 1.
    for k in range(1, L):
        model.addConstr(
            sum(y[i, i + k] for i in range(L - k + 1)) <= 1,
            name=f"UniqueLength[{k}]",
        )

    # Enforce y_ij == x_i AND x_k
    # For this problem we can get away with only enforcing
    # (x_i = 1 AND x_j = 1) -> y_ij = 1
    for (i, j), y_var in y.items():
        model.addConstr(x[i] + x[j] - 1 <= y_var)

    # Either require at least n marks, or try to maximize the number of marks.
    model.setOptionValue("time_limit", 300)
    model.addConstr(sum(x.values()) >= n, name="RequireNMarks")
    model.run()
    # model.maximize(sum(x.values()))

    info = model.getInfo()

    if info.primal_solution_status == SolutionStatus.kSolutionStatusFeasible:
        print("## Golomb Ruler Problem ##")
        print(f"L = {L}, n = {n}")
        sol = model.getSolution().col_value
        used_marks = [idx for idx, var in x.items() if sol[var.index] > 0]
        print(f"used_marks = {used_marks}")
