Your task in this exercise will be to familiarize youself with the NuSMV model checker and z3 SMT Solver. In particular, you will examine a number of LTL specifications, first using NuSMV, and then by performing a translation to SMT and applying z3.

To simplify our task of translating NuSMV to SMT later, we use a limited syntax. In particular, in your NuSMV encodings please only use a single MODULE and within it only VAR, INIT, TRANS, INVAR and LTLSPEC declarations.

## Exercises

When asked for explanations, please either add them as comments to the NuSMV output files or include them in a separate text or pdf file. Your submission for this exercise should contain the following files:
- `hanoi.smv` containing the encoding of the Tower of Hanoi puzzle with your explanations.
- `hanoi.out` containing the output of NuSMV on the file `hanoi.smv` with your explanations.
- `dogbunny.smv` containing the encoding of the dog bunny puzzle with your explanations.
- `dogbunny.out` containing the output of NuSMV on the file `dogbunny.smv` with your explanations.
- `short.txt`/`short.pdf` containing the answers to the questions in exercise 1.3.
- `ferryman.ipynb` containing the encoding of the wolf, goat and cabbage problem in SMT and your explanations.

### Exercise 1.1

Consider the following puzzle that is an instance of the puzzle known as the “Tower of Hanoi”. There are three poles (left, middle, right) and four ordered disks (d1, d2, d3, d4) of different sizes, with disk d1 being the biggest one. Initially, all four disks are on the left pole in ascending order, the smallest at the top. The goal of the puzzle is to move all four disks to the right pole, using
the following simple rules:
- Only one disk can be moved at a time;
- Each move consists of taking the upper disk from one of the poles and placing it on top of another
pole;
- No disk may be placed on top of a smaller disk.
The NuSMV specification in the file `examples/hanoi.smv` describes this puzzle. Explain the encoding of the puzzle. In particular, describe which rule each of the TRANS and INVAR statements encode.

Run NuSMV on the file `examples/hanoi.smv` and include the output in your submission. Explain the output. In particular, explain how the counter example corresponds to a solution of the puzzle.

### Exercise 1.2

In this exercise, you will use NuSMV to analyze the instance of the dog bunny puzzle by Conrad Barski which you can find in the example directory.

You can move a dog and two rabbits across a graph of locations. Some edges can only be traversed in one direction, some are annotated with conditions that must be fulfilled in order to traverse the edge. The goal is to reach the goal state, in which both rabbits are located at carrot and the dog is located at bone. Note that the number of animals at one particular location is not restricted. A solution to the
puzzle is a sequence of moves that reaches the goal state. Locations
are annotated with their identifiers, and the edge between house and tree is annotated with a conjunction of conditions.

The file `examples/dogbunny.smv` contains part of the encoding of the puzzle. Complete the encoding by adding the missing parts. Annotate our solution with explanations. Run NuSMV on the file `examples/dogbunny.smv` and include the output in your submission. Explain the output. In particular, explain how the counter example corresponds to a solution of the puzzle.

### Exercise 1.3

In the file `examples/short.smv` you will find a simple specification encoding access control to a resource, i.e. if the resource is ready and there is a request, then the resource is busy in the following state.

Check out and run the jupyter notebook `short.ipynb`. It contains an encoding of the same specification in SMT. Explain why one specification is valid while the other results in a counter example. Answer the following questions and justify your answers:
- Is it sufficient to check if the specification holds up to $k=10$?
- Would it be sufficient to only check $(k, l)$-loops in which $k = l$? (Hint: What is a _safety property_?)

### Exercise 1.4

In the file `examples/ferryman.smv` you will find a specification encoding the classic [wolf, goat and cabbage problem](https://en.wikipedia.org/wiki/Wolf,_goat_and_cabbage_problem). In the jupyter notebook `ferryman.ipynb`, encode the same specification in SMT as was done in `short.ipynb`. Explain which parts of the SMT encoding correspond to which parts of the NuSMV specification. Check if the specification holds up to $k=10, l=10$. Explain the output. In particular, explain how the counter example corresponds to a solution of the puzzle.
