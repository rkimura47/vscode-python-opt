import gurobipy as grb


def run_example(L: int, n: int):
    """Run Golomb ruler example.

    Args:
        L: Length of ruler
        n: Number of marks
    """
    with grb.Env() as env, grb.Model(env=env) as model:
        marks = range(L + 1)
        mark_pairs = [(i, j) for i in marks for j in marks if i < j]
        # x_i = 1 if mark i is chosen, 0 otherwise
        x = model.addVars(marks, vtype=grb.GRB.BINARY, name="x")
        # y_ij = 1 iff x_i = 1 AND x_k = 1
        y = model.addVars(mark_pairs, vtype=grb.GRB.BINARY, name="y")

        # Among all possible pairs of marks measuring length k, there can be at most 1.
        model.addConstrs(
            (
                grb.quicksum(y[i, i + k] for i in range(L - k + 1)) <= 1
                for k in range(1, L)
            ),
            "UniqueLength",
        )

        # Enforce y_ij == x_i AND x_k
        # For this problem we can get away with only enforcing
        # (x_i = 1 AND x_j = 1) -> y_ij = 1
        # but it solves much faster when we fully enforce AND
        for (i, j), y_var in y.items():
            model.addConstr(y_var == grb.and_(x[i], x[j]), f"AndPair[{i},{j}]")
            # model.addConstr(x[i] + x[j] - 1 <= y_var)

        # Either require at least n marks, or try to maximize the number of marks.
        model.addConstr(x.sum() >= n, "RequireNMarks")
        # model.setObjective(x.sum(), grb.GRB.MAXIMIZE)

        model.optimize()

        if model.SolCount > 0:
            print("## Golomb Ruler Problem ##")
            print(f"L = {L}, n = {n}")
            used_marks = [idx for idx, var in x.items() if var.x > 0]
            print(f"used_marks = {used_marks}")
