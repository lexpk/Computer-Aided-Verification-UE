In the second exercise, you will be implementing your own bounded model checker. In exercise 1, you have already encoded single instances of NuSMV specifications into SMT, and you are tasked to automate this process now.

## Exercise 2

Implement a bounded model checker for LTL formulas. Your submission may contain any number of python files, but should contain at least one jupyter-notebook named `demo.ipynb` that demonstrates the usage of your implementation. Your implementation should be able to read a NuSMV-like input file and check if the specification holds for all $(k, l)$-loops up to a given bound $k$.

Your implementation should support at least the following subset of NuSMV:
- You don't need to implement modules and can assume that there is only one `MODULE main`.
- Implement boolean variable declarations, e.g. `VAR x: boolean; y: boolean;`, and enum variable declarations, e.g. `VAR proc: {idle, entering, critical, exiting};`.
- You should implement `INIT`, `TRANS` and `INVAR` declarations, i.e.
    - `INIT proc = idle`
    - `TRANS proc = critical -> next(process) = {critical, exiting}`
    - `INVAR proc = critical -> x & y`
- Implement LTL specifications, e.g. `LTLSPEC G ! (proc = critical & proc = entering);`. You should support at least the following operators:
    - `X` (next)
    - `G` (globally)
    - `F` (finally)
    - `U` (until)
    - `!` (not)
    - `&` (and)
    - `|` (or)
    - `->` (implies)
- Support the following types of expressions:
    - Variables (anything declared with `VAR`, e.g. `x`, `y`, `proc`)
    - Constants (TRUE, FALSE, anything that is part of a finite domain)
    - Comparison operators `=`, `!=` between variables and constants (e.g. `x = y`, `proc != idle`)
    - Boolean combinations `!`, `&`, `|`, `->` between boolean variables, constants and comparisons (e.g. `x & (y | proc = idle)`)
    - Inclusion operator `in` between variables and sets (e.g. `proc in {idle, entering}`)

All files from exercise 1 fall into this subset. They have been included in the [`examples`](examples) folder. You can use these files to test your implementation.

For your convenience, I have included a parser for the specified subset of NuSMV. Its usage is demonstrated in the [`parse_demo.ipynb`](parse_demo.ipynb) notebook. A possible first step could be extending the class definitions in [`logic.py`](logic.py) with methods that convert the given constraints into z3 constraints, given parameters $k, l$.
