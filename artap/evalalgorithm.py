from abc import abstractmethod
import operator
from types import SimpleNamespace
from artap.results import Results
from artap.algorithm import Algorithm
from artap import evalfunctions as ef
import statistics
'''
TODO:
    - tests
    - abstracting
    - kwargs
    - stat. functions for vectors
'''
class AlgorithmEvaluation:

    def __init__(self, algorithm: Algorithm, dimension=3, **kwargs):
        self.dimension = dimension
        self.set_dimension(self.dimension)
        self.algorithm = algorithm

        self.results = {}
        self.nb_testrun = kwargs.pop("nb_testrun", 5)
        self.nb_iteration = kwargs.pop("nb_iter", 100)
        self.nb_individual = kwargs.pop("nb_individual", 10)

    def runtests(self):
        self.results.clear()
        self.set_dimension(self.dimension)

        for test in ef.testfactory:
            costs = list()
            vectors = list()

            for i in range(self.nb_testrun):
                problem = test(dimension=self.dimension)
                alg = self.algorithm(problem)
                problem.logger.disabled = True
                alg.run()
                c, v = self.get_results(problem)
                costs.append(c)
                vectors.append(v)

            self.results.setdefault(problem.name, SimpleNamespace())
            key = problem.name
            self.results[key].name = problem.name
            self.results[key].best_cost = self.get_best_cost(costs)
            self.results[key].worst_cost = self.get_worst_cost(costs)
            self.results[key].avg_cost = self.get_avg_cost(costs)
            self.results[key].std_cost = self.get_std_cost(costs)
            
            '''
            self.results[key].best_vector = self.get_best_vector(vectors)
            self.results[key].worst_vector = self.get_worst_vector(vectors)
            self.results[key].avg_vector = self.get_avg_vector(vectors)
            self.results[key].std_vector = self.get_std_vector(vectors)
            '''

            print(problem.name, 'Done')
            print(self.results[key])
            print('\n'*3)



    def set_dimension(self, dim):
        ef.TestFunctionBase.dimension = dim


    def get_results(self, problem):
        res = Results(problem).find_optimum()
        c = list(res.costs)
        v = list(res.vector)
        return c, v

    def get_best_cost(self, costs):
        return min(costs, key=lambda ci: ci[0])

    def get_worst_cost(self, costs):
        return max(costs, key=lambda ci: ci[0])

    def get_avg_cost(self, costs):
        return statistics.fmean(map(operator.itemgetter(0), costs))

    def get_std_cost(self, costs):
        return statistics.stdev(map(operator.itemgetter(0), costs))
    
    def __call__(self):
        self.runtests()

if __name__=='__main__':
    # for testing
    from artap.algorithm_swarm import OMOPSO
    from artap.benchmark_functions import Ackley

    ef.testfactory.append(Ackley)

    test1 = AlgorithmEvaluation(OMOPSO, 3)
    test1()
