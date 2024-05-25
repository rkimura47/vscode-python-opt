from ortools.sat.python import cp_model


def run_example(L: int, n: int):
    """Run Golomb ruler example using CP model.

    When using CP-SAT, the CP model seems to be slightly better than the MIP model.
    This model is based on golomb_sat.py in the or-tools Python examples.

    Args:
        L: Length of ruler
        n: Number of marks
    """
    model = cp_model.CpModel()

    marks = range(n)
    mark_pairs = [(i, j) for i in marks for j in marks if i < j]
    # x_i = location of the i-th mark
    x = [model.new_int_var(0, L, name=f"x[{i}]") for i in marks]
    # y_ij = distance between the i-th mark and j-th mark (x_i and x_j)
    y = {
        pair: model.new_int_var(0, L, name=f"y[{pair[0]},{pair[1]}]")
        for pair in mark_pairs
    }

    # Order marks from smallest to largest.
    model.add(x[0] == 0)
    for i in marks[1:]:
        model.add(x[i] > x[i - 1])

    # Enforce y_ij == x[j] - x[i].
    for (i, j), y_var in y.items():
        model.add(y_var == x[j] - x[i])

    # The distances between pairs of marks must all be different.
    model.add_all_different(y.values())

    # Simple symmetry breaking
    if n > 2:
        model.add(y[n - 2, n - 1] > y[0, 1])

    solver = cp_model.CpSolver()
    solver.parameters.log_search_progress = True
    status = solver.solve(model)

    # mypy with strict equality enabled complains here because cp_model.CpSolver.solve(...) returns a CpSolverStatus,
    # but cp_model.OPTIMAL is a CpSolverStatus.ValueType.
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):  # type: ignore[comparison-overlap]
        print("## Golomb Ruler Problem ##")
        print(f"L = {L}, n = {n}")
        used_marks = [solver.value(x_var) for x_var in x]
        print(f"used_marks = {used_marks}")
