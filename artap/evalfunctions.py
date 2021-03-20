from artap.problem import Problem
from math import sqrt, exp, sin, cos, pi, e
from artap.results import Results


'''
Jamian, J. J. & Abdullah, Mohd Noor & Mokhlis, Hazlie & Mustafa, Mohd & Abu Bakar, Ab Halim. (2014).
Global Particle Swarm Optimization for High Dimension Numerical Functions Analysis.
Journal of Applied Mathematics. 2014. 1-14. 10.1155/2014/329193. 
'''

''' TODO 
    - Writing tests
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
        string += 'vector: ' + ' '.join([f'{xi:.7f}'for xi in v]) + '\n'
        string += f'costs: ' + ' '.join([f'{xi:.7f}'for xi in c]) + '\n'
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
        for i, xi in enumerate(individual.vector):
            f += (xi ** 2) * 10e6 ** (i / (self.dim - 1))
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
        f = 0.0
        for xi in individual.vector:
            f += (xi + 0.5) ** 2

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
        f = 0.0
        lambda1 = 0.0
        lambda2 = 0.0
        for xi in individual.vector:
            lambda1 += xi ** 2
            lambda2 += cos(2 * pi * xi)

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
        f = 0.0

        for xi in individual.vector:
            f += xi **2 - 10 * cos(2 * pi * xi) + 10

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
        f = 0.0

        for xi in individual.vector:
            yi = 0.0
            if abs(xi) < 0.5:
                yi = xi
            else:
                yi = round(2 * xi) / 2

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
        f = 0.0

        for xi in individual.vector:
            f += xi ** 4 - 16 * xi ** 2 + 5 * xi

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
        f = 0.0

        for xi in individual.vector: 
            f += abs(xi * sin(xi + 0.1 * xi))

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
        f = 0.0

        for xi in individual.vector:
            f += (xi - 1) ** 2 * abs(1 + xi * sin(3*pi*xi)**2)

        return [f]

if __name__ == '__main__':
    # for testing
    from artap.algorithm_swarm import OMOPSO
    
    TestFunction.dim = 3
    
    testfunctions = [
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

    for test in testfunctions:
        algorithm = OMOPSO(test)
        algorithm.run()
        print(test)
