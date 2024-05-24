from docplex.mp.model import Model


def run_example(L: int, n: int):
    """Run Golomb ruler example.

    Args:
        L: Length of ruler
        n: Number of marks
    """
    with Model(log_output=True) as m:
        marks = range(L + 1)
        mark_pairs = [(i, j) for i in marks for j in marks if i < j]
        # x_i = 1 if mark i is chosen, 0 otherwise
        x = m.binary_var_dict(marks, name="x")
        # y_ij = 1 iff x_i = 1 AND x_k = 1
        y = m.binary_var_dict(mark_pairs, name="y")

        # Among all possible pairs of marks measuring length k, there can be at most 1.
        m.add_constraints(
            (
                m.sum_vars_all_different(y[i, i + k] for i in range(L - k + 1)) <= 1
                for k in range(1, L)
            ),
            "UniqueLength",
        )

        # Enforce y_ij == x_i AND x_k
        # For this problem we can get away with only enforcing
        # (x_i = 1 AND x_j = 1) -> y_ij = 1
        # but it solves much faster when we fully enforce AND
        # Note: the inequality version seems to play better with model size limits.
        for (i, j), y_var in y.items():
            # m.add_constraint(y_var == m.logical_and(x[i], x[j]), f"AndPair[{i},{j}]")
            m.add_constraint(x[i] + x[j] - 1 <= y_var)

        # Either require at least n marks, or try to maximize the number of marks.
        m.add_constraint(m.sum_vars_all_different(x.values()) >= n, "RequireNMarks")
        # m.maximize(m.sum_vars_all_different(x.values()))

        solve_solution = m.solve()

        if solve_solution:
            print("## Golomb Ruler Problem ##")
            print(f"L = {L}, n = {n}")
            used_marks = [idx for idx, var in x.items() if var in solve_solution]
            print(f"used_marks = {used_marks}")