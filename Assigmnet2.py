"""TODO 2)	Write a short and most efficient python function with the next description
Input:
formula - a text with a valid mathematical formula on three arguments: A,B and C
n - number of times to evaluate, default 100
This function should random n times values for A, B and C and evaluate the formula result.
 For each evaluation print the formula and the result
 Example:
"""
import random as r


def test_value():
    yield r.randint(-100,100)


def formula_validation(formula, n=100):
    variables = ["A","B","C"]
    for _ in range(n):
        for v in variables:
            print(formula)
            formula = formula.replace(v, str(next(test_value())))
        print(formula)
        result = eval(formula)

        print(formula + "=" + str(result))


formula_validation(formula="2*A+B",n=2)
# Output (possible):
# 2*3+5 = 11
# 2*12+49 = 73
