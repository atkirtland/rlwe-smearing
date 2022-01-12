# rlwe-smearing
Code for the paper "The Polynomial Learning With Errors Problem and the Smearing Condition"

`smearing-submission.ipynb` contains code to generate Figures 1, 2, 4, and 5 in the paper, and thus can generate the mapped distributions and the probability curves.
`figure2.py` and `plot_figure_2.py` contain code to generate Figure 3 in the paper.

We will also remark that one can use Sagemath to find polynomials that fit the parameters of the problem. 
First, think of a polynomial and check that it is irreducible, e.g. by

```python
R=ZZ['x']                                                                                          
x = R.gen()
(x^5-6*x+2).is_irreducible()
```

next, one can find the roots of the polynomial in Z_q, e.g. by

```python
Q=101
for i in range(Q):
  if Mod((x^5-6*x+2)(i),Q)==0:
    print(i)
```
