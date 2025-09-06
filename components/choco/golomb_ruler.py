from pychoco import Model


def run_example(L: int, n: int):
    model = Model()

    marks = range(n)
    mark_pairs = [(i, j) for i in marks for j in marks if i < j]
    # x_i = location of the i-th mark
    x = model.intvars(n, 0, L, name="x")
    # y_ij = distance between the i-th mark and j-th mark (x_i and x_j)
    y = {
        pair: model.intvar(0, L, name=f"y[{pair}]")
        for pair in mark_pairs
    }

    # Enforce y_ij == x[j] - x[i].
    for pair in mark_pairs:
        # Using distance() instead of arithm() here actually helps a lot!
        model.distance(x[pair[0]], x[pair[1]], "=",y[pair]).post()

    # Order marks from smallest to largest.
    model.arithm(x[0], "=", 0).post()
    model.increasing(x, 1).post()

    # The distances between pairs of marks must all be different.
    model.all_different(list(y.values())).post()

    # Simple symmetry breaking
    if n > 2:
        model.arithm(y[n - 2, n - 1], ">", y[0, 1]).post()

    solver = model.get_solver()
    # These search strategies seem to give the best results.
    solver.set_input_order_lb_search(x)
    # solver.set_dom_over_w_deg_ref_search(x)
    # solver.set_failure_length_based_search(x)

    # solver.show_short_statistics()
    solver.show_statistics()
    solve_solution = solver.find_solution(time_limit="300s")

    if solve_solution:
        print("## Golomb Ruler Problem ##")
        print(f"L = {L}, n = {n}")
        used_marks = [solve_solution.get_int_val(x_var) for x_var in x]
        print(f"used_marks = {used_marks}")
