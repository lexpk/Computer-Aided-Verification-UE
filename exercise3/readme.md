For exercise 3 you are to extend your implementation from exercise 2 to support additional features. Include the presentation of your additional features in the notebook `demo.ipynb` or an additional notebook. Here are some ideas for extensions, but you are free to come up with your own:

### Until and Release Operators

Implement the Until and Release operators. The file [`examples/ferrymanuntil.smv`](examples/ferrymanuntil.smv) contains an encoding of the ferryman problem using the Until operator. Come up with an example using the Release operator. Note that [NuSMV](https://nusmv.fbk.eu/userman/v26/nusmv.pdf) uses the symbol `V` to denote the release operator.

### Past Operators

Implement (at least) the past operators `Y` (previous), `H` (historrically) and `O` (once).  Come up with examples using past operators.

### Fairness Constraints

Implement fairness constraints as described in the [NuSMV user guide](https://nusmv.fbk.eu/userman/v26/nusmv.pdf). You can find an example in the [`examples`](examples) folder, which describes (faulty) mutual exclusion between two processes. However, due to the fairness constraint the second LTLSPEC, i.e. the _liveness property_, does hold.

### Integer Arithmetic

Implement an integer datatype and arithmetic operations (+, -, *, /, mod). You can find an example of a simple counter that is incremented and reset in [`examples/counter.smv`](examples/counter.smv). An interesting application could be identifying the [Zune Bug](http://bit-player.org/2009/the-zune-bug) by encoding the C program into NuSMV and checking an appropriate LTL formula.
