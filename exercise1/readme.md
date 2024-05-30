Your task in this exercise will be to familiarize youself with the NuSMV Model checker and a SAT-Solver of your choice.

## 1.1. NuSMV

NuSMV is a symbolic model checker for finite state systems, in particular it implements LTL model checking as you will be implementing. Please refer to the [NuSMV Manual](https://nusmv.fbk.eu/tutorial/v26/tutorial.pdf) for a detailed introduction to the tool. In Section 5 the LTL model checking functionality is explained.

### 1.1.1. Exercises

You will find a number of example specifications in the `examples` directory. Please explain the defined state transition system and the LTL formula in each of the examples. Then, run NuSMV on the examples and check if the LTL formula holds. Explain the output of NuSMV.

## 1.2. SAT-Solver

You can choose any SAT-Solver you like. If you use python, we recommend using the `pysat` library. You can install it by running:

```bash
pip install pysat
```