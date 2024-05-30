In the second exercise, you will be implementing your own bounded model checker. You will be provided with a template in Python, which you can use as a starting point. You can implement the exercises in any programming language you like. However, we highly recommend using a language which tightly interfaces some SAT solver, such as Python, C, C++ or Java. This will make your life much easier in exercises 3 and 4.

## 2.1. Exercise 2

You may use the [lecture notes of Fabio Somenzi](https://tuwel.tuwien.ac.at/pluginfile.php/3960980/mod_resource/content/1/fv.pdf) as a reference, although we will be going beyond them.

### 2.1.1. Task 1

Implement a bounded model checker for LTL formulas. In `examples`, you will find a number of specifications given in the NuSMV format. Your task is implementing a procedure which takes such a specification and a bound `k` and returns whether the specification holds for any path of length `k`. Use a reduction to SAT and a SAT solver to solve this problem.

Your implementation should support the following subset of NuSMV:
- You don't need to implement modules and can assume that there is only one `MODULE main`.
- Implement boolean variables, e.g. `VAR x: boolean; y: boolean;`, and variables over finite domains, e.g. `VAR proc: {idle, entering, critical, exiting};`.
- You should implement assignments for initial and next states, e.g. `init(proc) := idle; next(proc) := ...;`.
- Implement LTL formulas, e.g. `LTLSPEC G ! (proc = critical & proc = entering);`. You should support at least the following operators:
    - `X` (next)
    - `G` (globally)
    - `F` (finally)
    - `U` (until)
    - `R` (release)
    - `!` (not)
    - `&` (and)
    - `|` (or)
    - `->` (implies)
    - `<->` (iff)
- Support the following types of expressions:
    - Variables (anything declared with `VAR`, e.g. `x`, `y`, `proc`)
    - Constants (TRUE, FALSE, anything that is part of a finite domain)
    - Comparison operators `=`, `!=` between variables and constants (e.g. `x = y`, `proc != idle`)
    - Boolean combinations `!`, `&`, `|`, `->`, `<->` between boolean variables, constants and comparisons (e.g. `x & (y | proc = idle)`)
    - case expressions, e.g.
    ```
        case
            proc = idle : {idle, entering};
            proc = entering : critical;
            proc = critical : {critical, exiting};
            proc = exiting : idle;
        esac;
    ```

Note that in your implementation you may reduce the temporal operators and logical connectives to a smaller set of operators, e.g. `F p` can be reduced to `TRUE U p`.
