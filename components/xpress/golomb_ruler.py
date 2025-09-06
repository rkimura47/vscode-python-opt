import xpress as xp
from xpress.enums import MIPStatus


def add_and_pair_constraints_to_model(
    model: xp.problem, x: dict[int, xp.var], y: dict[tuple[int, int], xp.var]
) -> None:
    contype = []
    resultant = []
    colstart = []
    colind = []
    col_index = 0
    for (i, j), y_var in y.items():
        contype.append(xp.gencons_and)
        resultant.append(y_var)
        colstart.append(col_index)
        colind.extend([x[i], x[j]])
        col_index += 2

    model.addgencons(
        contype=contype,
        resultant=resultant,
        colstart=colstart,
        colind=colind,
        valstart=None,
        val=None,
    )


def run_example(L: int, n: int):
    """Run Golomb ruler example.

    Args:
        L: Length of ruler
        n: Number of marks
    """
    with xp.problem() as model:
        marks = range(L + 1)
        mark_pairs = [(i, j) for i in marks for j in marks if i < j]
        # x_i = 1 if mark i is chosen, 0 otherwise
        x = model.addVariables(marks, vartype=xp.binary, name="x")
        # y_ij = 1 iff x_i = 1 AND x_k = 1
        y = model.addVariables(mark_pairs, vartype=xp.binary, name="y")

        # Among all possible pairs of marks measuring length k, there can be at most 1.
        model.addConstraint(
            xp.constraint(
                xp.Sum(y[i, i + k] for i in range(L - k + 1)) <= 1,
                name=f"UniqueLength[{k}]",
            )
            for k in range(1, L)
        )

        # Enforce y_ij == x_i AND x_k
        # For this problem we can get away with only enforcing
        # (x_i = 1 AND x_j = 1) -> y_ij = 1
        # but it solves much faster (and works better with model limits) when we fully enforce AND
        add_and_pair_constraints_to_model(model, x, y)
        # model.addConstraint(x[i] + x[j] - 1 <= y_var for (i, j), y_var in y.items())

        # Either require at least n marks, or try to maximize the number of marks.
        # It's a little annoying that xp.Sum() doesn't recognize view objects as iterators.
        model.addConstraint(
            xp.constraint(xp.Sum(iter(x.values())) >= n, name="RequireNMarks")
        )
        # model.setObjective(xp.Sum(iter(x.values())), sense=xp.maximize)

        model.mipoptimize()

        if model.attributes.mipstatus in (MIPStatus.OPTIMAL, MIPStatus.SOLUTION):
            print("## Golomb Ruler Problem ##")
            print(f"L = {L}, n = {n}")
            sol = model.getSolution(x)
            used_marks = [idx for idx, val in sol.items() if val > 0]
            print(f"used_marks = {used_marks}")
