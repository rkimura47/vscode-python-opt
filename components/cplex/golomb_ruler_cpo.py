from docplex.cp.model import CpoModel


def run_example(L: int, n: int):
    """Run Golomb ruler example using CP model.

    When using docplex, the CP model plays much better with model size limits
    compared to the MIP model.
    This model is based on "Model a Golomb ruler using DO.ipynb" in the
    IBMDecisionOptimization/DO-Samples github repository.

    Args:
        L: Length of ruler
        n: Number of marks
    """
    with CpoModel() as mdl:
        marks = range(n)
        mark_pairs = [(i, j) for i in marks for j in marks if i < j]
        # x_i = location of the i-th mark
        x = mdl.integer_var_list(n, 0, L, name="x")
        # y_ij = distance between the i-th mark and j-th mark (x_i and x_j)
        y = {
            pair: x[pair[1]] - x[pair[0]]
            for pair in mark_pairs
        }

        # Order marks from smallest to largest.
        mdl.add(x[0] == 0)
        for i in marks[1:]:
            mdl.add(x[i] > x[i - 1])

        # The distances between pairs of marks must all be different.
        mdl.add(mdl.all_diff(y.values()))

        # Simple symmetry breaking
        if n > 2:
            mdl.add(y[n - 2, n - 1] > y[0, 1])

        solve_solution = mdl.solve()

        if solve_solution:
            print("## Golomb Ruler Problem ##")
            print(f"L = {L}, n = {n}")
            used_marks = [solve_solution[x_var] for x_var in x]
            print(f"used_marks = {used_marks}")
