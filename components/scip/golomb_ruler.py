import pyscipopt as scip


def run_example(L: int, n: int):
    """Run Golomb ruler example.

    Args:
        L: Length of ruler
        n: Number of marks
    """
    model = scip.Model()

    marks = range(L + 1)
    mark_pairs = [(i, j) for i in marks for j in marks if i < j]
    # x_i = 1 if mark i is chosen, 0 otherwise
    x = {m: model.addVar(vtype="B", name=f"x[{m}]") for m in marks}
    # y_ij = 1 iff x_i = 1 AND x_k = 1
    y = {
        pair: model.addVar(vtype="B", name=f"y[{pair[0]},{pair[1]}]")
        for pair in mark_pairs
    }

    model.addConss(
        (
            scip.quicksum(y[i, i + k] for i in range(L - k + 1)) <= 1
            for k in range(1, L)
        ),
        "UniqueLength",
    )

    # Enforce y_ij == x_i AND x_k
    # For this problem we can get away with only enforcing
    # (x_i = 1 AND x_j = 1) -> y_ij = 1
    # but it solves much faster when we fully enforce AND
    for (i, j), y_var in y.items():
        model.addConsAnd([x[i], x[j]], y_var, f"AndPair[{i},{j}]")
        # model.addCons(x[i] + x[j] - 1 <= y_var)

    # Either require at least n marks, or try to maximize the number of marks.
    model.addCons(scip.quicksum(x.values()) >= n, "RequireNMarks")
    # model.setObjective(scip.quicksum(x.values()), grb.GRB.MAXIMIZE)

    model.optimize()

    if model.getNSolsFound() > 0:
        print("## Golomb Ruler Problem ##")
        print(f"L = {L}, n = {n}")
        used_marks = [idx for idx, var in x.items() if model.getVal(var) > 0]
        print(f"used_marks = {used_marks}")
