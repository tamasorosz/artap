from artap.problem import Problem
from math import sqrt, exp, sin, cos, pi, e
from artap.results import Results
import functools
from collections import deque


'''
Jamian, J. J. & Abdullah, Mohd Noor & Mokhlis, Hazlie & Mustafa, Mohd & Abu Bakar, Ab Halim. (2014).
Global Particle Swarm Optimization for High Dimension Numerical Functions Analysis.
Journal of Applied Mathematics. 2014. 1-14. 10.1155/2014/329193. 
'''

''' TODO 
    - Writing tests
    - changeable population size, nb_iteration
'''

testfactory = deque()

class TestFunctionBase(Problem):

    dim = 3


    def get_results(self):
        res = Results(self).find_optimum()
        self.vector = list(res.vector)
        self.costs = list(res.costs)
        return self.vector, self.costs

    def __str__(self) -> str:
        v, c = self.get_results()
        string = '\n' + '-'*40 + '\n'
        string += f' name: {self.name}\n'
        string += ' vector: ' + ' '.join([f'{xi:.7f}'for xi in v]) + '\n'
        string += f' costs: ' + ' '.join([f'{xi:.7f}'for xi in c]) + '\n'
        string += "-"*40 + '\n'
        return string


def register(name: str, ranges: tuple):
    def decorator(func):
        class TestFunction(TestFunctionBase):
            def set(self, **kwargs):
                self.logger.disabled = True
                self.name = name
                self.parameters = list()
                for dim in range(1, TestFunctionBase.dim + 1):
                    self.parameters.append({
                        'name': f'x_{dim}',
                        'bounds': ranges
                        })

                self.costs = [{
                    'name':self.name,
                    'criteria': 'minimize'
                    }]
            
            @functools.wraps(func)
            def evaluate(self, individual):
                return [func(individual.vector)]

            def __hash__(self):
                return id(self)


        testfactory.append(TestFunction)

        return func

    return decorator


@register(name='F1', ranges=(-100.0, 100.0))
def f1(x):
    return sum(map(lambda xi: xi**2, x))

@register("F2", (-100.0, 100.0))
def f2(x):
    f = 0.0
    dim = TestFunctionBase.dim
    for i in range(dim):
        f += (x[i] ** 2) * 10e6 ** (i / (dim - 1))

    return f


@register('F3', (-100.0, 100.0))
def f3(x):
    f = 0.0
    for i in range(1, TestFunctionBase.dim + 1):
        f += i * x[i - 1] ** 2

    return f


@register('F4', (-10.0, 10.0))
def f4(x):
    f = 0.0
    for i in range(1, TestFunctionBase.dim + 1):
        f += abs(x[i - 1]) ** (i + 1)
    return f


@register('F5', (-10.0, 10.0))
def f5(x):
    f = 0.0
    for i in range(1, TestFunctionBase.dim + 1):
        f += (x[i - 1] + 0.5) ** 2

    return f


# debug
@register('F6', (-32.0, 32.0))
def f6(x):
    f = 0.0
    lambda1 = 0.0
    lambda2 = 0.0
    for i in range(TestFunctionBase.dim):
        lambda1 += x[i] ** 2
        lambda2 += cos(2 * pi * x[i])

        lambda1 *= -0.2 * sqrt(1 / TestFunctionBase.dim)
        lambda2 *= 1 / TestFunctionBase.dim

        f = -20 * exp(lambda1) - exp(lambda2) + 20 + e
    return f


@register('F7', (-10.0, 10.0))
def f7(x):
    f = 0.0
    for i in range(1, TestFunctionBase.dim):
        f += 100 * (x[i] - x[i-1])**2 + (x[i-1]-1)**20

    return f

@register('F8', (-5.12, 5.12))
def f8(x):
    f = 0.0
    for xi in x:
        f += xi **2 - 10 * cos(2 * pi * xi) + 10

    return f

@register('F9', (-5.12, 5.12))
def f9(x):
    f = 0.0
    for i in range(TestFunctionBase.dim):
        yi = 0.0
        if abs(x[i]) < 0.5:
            yi = x[i]
        else:
            yi = round(2 * x[i]) / 2

        f += yi**2 - 10 * cos(2 * pi * yi) + 10

    return f

#debug
@register('F10', (-5.0, 5.0))
def f10(x):
    f = 0.0
    for xi in x:
        f += xi ** 4 - 16 * xi ** 2 + 5 * xi
    return f / TestFunctionBase.dim

@register('F11', (-10.0, 10.0))
def f11(x):
    f = 0.0
    for xi in x:
        f += abs(xi * sin(xi) + 0.1 * xi)
    return f

@register('F12', (-10.0, 10.0))
def f12(x):
    f = 0.0
    for xi in x:
        f += (xi - 1) ** 2 * abs(1 + xi * sin(3*pi*xi)**2)

    return f

if __name__ == '__main__':
    # for testing
    from artap.algorithm_swarm import OMOPSO
    TestFunctionBase.dim = 3

    l = range(3)
    print(f1(l))
    for test in testfactory:
        problem = test()
        alg = OMOPSO(problem)
        alg.run()
        print(problem)


