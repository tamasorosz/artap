from artap.problem import Problem
from math import sqrt, exp, sin, cos, pi, e
from artap.results import Results


'''
Jamian, J. J. & Abdullah, Mohd Noor & Mokhlis, Hazlie & Mustafa, Mohd & Abu Bakar, Ab Halim. (2014).
Global Particle Swarm Optimization for High Dimension Numerical Functions Analysis.
Journal of Applied Mathematics. 2014. 1-14. 10.1155/2014/329193. 
'''

class TestFunction(Problem):

    dim = 3


    def get_results(self):
        res = Results(self).find_optimum()
        self.vector = list(res.vector)
        self.costs = list(res.costs)
        return self.vector, self.costs

    def __str__(self) -> str:
        v, c = self.get_results()
        string = '\n' + '-'*40 + '\n'
        string += f'name: {self.name}\n'
        string += 'vector: ' + ' '.join([f'{xi:.3f}'for xi in v])
        string += f'\ncosts: ' + ' '.join([f'{xi:.3f}'for xi in c]) + '\n'
        string += "-"*40 + '\n'
        return string


class TestFunctionF1(TestFunction):

    def set(self, **kwargs):
        self.name = "F1"
        self.parameters = []
        for dim_i in range(1, self.dim + 1):
            self.parameters.append({
                'name': f'x_{dim_i}', 'bounds': [-100.0, 100.0]
            })
        self.costs = [{'name': 'F1', 'criteria': 'minimize'}]

    def evaluate(self, individual):
        return [sum(map(lambda x: x**2, individual.vector))]


class TestFunctionF2(TestFunction):

    def set(self, **kwargs):
        self.name = "F2"
        self.parameters = []
        for dim_i in range(1, self.dim + 1):
            self.parameters.append({
                'name': f'x_{dim_i}', 'bounds': [-100.0, 100.0]
            })
        self.costs = [{'name': 'F2', 'criteria': 'minimize'}]

    def evaluate(self, individual):
        x = individual.vector
        f = 0.0
        for i in range(self.dim):
            f += (x[i] ** 2) * 10e6 ** (i / (self.dim - 1))
        return [f]


class TestFunctionF3(TestFunction):

    def set(self, **kwargs):
        self.name = "F3"
        self.parameters = []
        for dim_i in range(1, self.dim + 1):
            self.parameters.append({
                'name': f'x_{dim_i}', 'bounds': [-10.0, 10.0]
            })
        self.costs = [{'name': 'F3', 'criteria': 'minimize'}]

    def evaluate(self, individual):
        x = individual.vector
        f = 0.0
        for i in range(1, self.dim + 1):
            f += i * x[i - 1] ** 2

        return [f]


class TestFunctionF4(TestFunction):

    def set(self, **kwargs):
        self.name = "F4"
        self.parameters = []
        for dim_i in range(1, self.dim + 1):
            self.parameters.append({
                'name': f'x_{dim_i}', 'bounds': [-10.0, 10.0]
            })
        self.costs = [{'name': 'F4', 'criteria': 'minimize'}]

    def evaluate(self, individual):
        x = individual.vector
        f = 0.0
        for i in range(1, self.dim + 1):
            f += abs(x[i - 1]) ** (i + 1)

        return [f]


class TestFunctionF5(TestFunction):

    def set(self, **kwargs):
        self.name = "F5"
        self.parameters = []
        for dim_i in range(1, self.dim + 1):
            self.parameters.append({
                'name': f'x_{dim_i}', 'bounds': [-10.0, 10.0]
            })
        self.costs = [{'name': 'F5', 'criteria': 'minimize'}]

    def evaluate(self, individual):
        x = individual.vector
        f = 0.0
        for i in range(1, self.dim + 1):
            f += (x[i - 1] + 0.5) ** 2

        return [f]


class TestFunctionF6(TestFunction):

    def set(self, **kwargs):
        self.name = "F6"
        self.parameters = []
        for dim_i in range(1, self.dim + 1):
            self.parameters.append({
                'name': f'x_{dim_i}', 'bounds': [-32.0, 32.0]
            })
        self.costs = [{'name': 'F6', 'criteria': 'minimize'}]

    def evaluate(self, individual):
        x = individual.vector
        f = 0.0
        lambda1 = 0.0
        lambda2 = 0.0
        for i in range(self.dim):
            lambda1 += x[i] ** 2
            lambda2 += cos(2 * pi * x[i])

        lambda1 *= -0.2 * sqrt(1 / self.dim)
        lambda2 *= 1 / self.dim

        f = -20 * exp(lambda1) - exp(lambda2) + 20 + e

        return [f]


class TestFunctionF7(TestFunction):

    def set(self, **kwargs):
        self.name = "F7"
        self.parameters = []
        for dim_i in range(1, self.dim + 1):
            self.parameters.append({
                'name': f'x_{dim_i}', 'bounds': [-10.0, 10.0]
            })
        self.costs = [{'name': 'F7', 'criteria': 'minimize'}]

    def evaluate(self, individual):
        x = individual.vector
        f = 0.0

        for i in range(1, self.dim):
            f += 100 * (x[i] - x[i-1])**2 + (x[i-1]-1)**2

        return [f]


class TestFunctionF8(TestFunction):

    def set(self, **kwargs):
        self.name = "F8"
        self.parameters = []
        for dim_i in range(1, self.dim + 1):
            self.parameters.append({
                'name': f'x_{dim_i}', 'bounds': [-5.12, 5.12]
            })
        self.costs = [{'name': 'F8', 'criteria': 'minimize'}]

    def evaluate(self, individual):
        x = individual.vector
        f = 0.0

        for i in range(self.dim):
            f += x[i] **2 - 10 * cos(2 * pi * x[i]) + 10

        return [f]


class TestFunctionF9(TestFunction):

    def set(self, **kwargs):
        self.name = "F9"
        self.parameters = []
        for dim_i in range(1, self.dim + 1):
            self.parameters.append({
                'name': f'x_{dim_i}', 'bounds': [-5.12, 5.12]
            })
        self.costs = [{'name': 'F9', 'criteria': 'minimize'}]

    def evaluate(self, individual):
        x = individual.vector
        f = 0.0

        for i in range(self.dim):
            yi = 0.0
            if abs(x[i]) < 0.5:
                yi = x[i]
            else:
                yi = round(2 * x[i]) / 2

            f += yi**2 - 10 * cos(2 * pi * yi) + 10

        return [f]


class TestFunctionF10(TestFunction):

    def set(self, **kwargs):
        self.name = "F10"
        self.parameters = []
        for dim_i in range(1, self.dim + 1):
            self.parameters.append({
                'name': f'x_{dim_i}', 'bounds': [-5.0, 5.0]
            })
        self.costs = [{'name': 'F10', 'criteria': 'minimize'}]

    def evaluate(self, individual):
        x = individual.vector
        f = 0.0

        for i in range(self.dim):
            f += x[i] ** 4 - 16 * x[i] ** 2 + 5 * x[i]

        return [1 / self.dim * f]


class TestFunctionF11(TestFunction):

    def set(self, **kwargs):
        self.name = "F11"
        self.parameters = []
        for dim_i in range(1, self.dim + 1):
            self.parameters.append({
                'name': f'x_{dim_i}', 'bounds': [-10.0, 10.0]
            })
        self.costs = [{'name': 'F11', 'criteria': 'minimize'}]

    def evaluate(self, individual):
        x = individual.vector
        f = 0.0

        for i in range(self.dim):
            f += abs(x[i] * sin(x[i]) + 0.1 * x[i])

        return [f]


class TestFunctionF12(TestFunction):

    def set(self, **kwargs):
        self.name = "F12"
        self.parameters = []
        for dim_i in range(1, self.dim + 1):
            self.parameters.append({
                'name': f'x_{dim_i}', 'bounds': [-10.0, 10.0]
            })
        self.costs = [{'name': 'F12', 'criteria': 'minimize'}]

    def evaluate(self, individual):
        x = individual.vector
        f = 0.0

        for i in range(self.dim):
            f += (x[i] - 1) ** 2 * abs(1 + x[i] * sin(3*pi*x[i])**2)

        return [f]

if __name__ == '__main__':
    # for testing
    from artap.algorithm_swarm import OMOPSO
    
    TestFunction.dim = 3
    
    problems = [
            TestFunctionF1(),
            TestFunctionF2(),
            TestFunctionF3(),
            TestFunctionF4(),
            TestFunctionF5(),
            TestFunctionF5(),
            TestFunctionF7(),
            TestFunctionF8(),
            TestFunctionF9(),
            TestFunctionF10(),
            TestFunctionF11(),
            TestFunctionF12(),
            ]

    for problem in problems:
        algorithm = OMOPSO(problem)
        algorithm.run()
        print(problem)
