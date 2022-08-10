# Fibonacci presentation

Academic presentation _(in French)_ on the numeric computation of the Fibonacci sequence $(F_n)_{n \in \mathbb{N}}$ defined as follows : $F_0 = 0$, $F_1 = 1$ and :

$$\forall n \geq 2, \ F_{n+2} = F_{n+1} + F_n$$

**Main issue** : How to compute Fibonacci sequence in the most powerful way ?

**Execution of sample/plotting script** :
```bash
pip install matplotlib # unique Python dependency
python3 script.py
```

## Table of contents

- Naive and iterative approaches
    - Recursion formula
    - Explicit method
- Recursion, a good lead ?
    - Implementation attempt
    - Comparison of iterative and recursive methods
- A last track : matrix writing
    - General presentation of the used method
    - Choice of fast exponentiation method
    - Implementation for calculating quantities $F_n$
- Conclusion & Answer to the problem
- Appendix : Application of $F_n$ &bull; Euclid's algorithm


**Main reference** : Based on *Arnaud de Saint Julien*'s paper : *[Escapade algorithmique avec Fibonacci](http://desaintar.free.fr/exposes/fibonacci.pdf)*

## Author

Lucas RODRIGUEZ (MPSI - 2018/2019)