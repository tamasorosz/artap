from abc import abstractmethod
from artap.results import Results
from artap.algorithm import Algorithm
from artap import evalfunctions as ef
import statistics
from types import SimpleNamespace

'''
TODO:
    - tests
    - abstracting
    - kwargs
    - min,max,avg,std / dimension for vectors
'''


class AlgorithmEvaluation:

    def __init__(self, algorithm: Algorithm, dimension=3, **kwargs):
        self.dimension = dimension
        self.set_dimension(self.dimension)
        self.algorithm = algorithm

        self.results = {}
        self.testresults = list()
        self.nb_testrun = kwargs.pop("nb_testrun", 5)
        self.nb_iteration = kwargs.pop("nb_iter", 100)
        self.nb_individual = kwargs.pop("nb_individual", 10)

    def runtests(self):
        self.results.clear()
        self.set_dimension(self.dimension)

        for test in ef.testfactory:
            self.testresults.clear()
            for i in range(self.nb_testrun):
                problem = test(dimension=self.dimension)
                alg = self.algorithm(problem)
                problem.logger.disabled = True
                alg.run()
                self.testresults.append(self.get_results(problem))            
            
            key = problem.name
            self.results.setdefault(key, SimpleNamespace())
            self.sort_testresults() # !!!!!!!
            self.results[key].name = problem.name

            # statistics
            self.set_min_costs(key)
            self.set_max_costs(key)
            self.set_avg_costs(key)
            self.set_std_costs(key)


            self.set_min_vector(key)
            self.set_max_vector(key)
            #self.set_d_min_vector(key)
            #self.set_d_max_vector(key)
            #self.set_d_avg_vector(key)
            #self.set_d_std_vector(key)

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

    @abstractmethod
    def sort_testresults(self):
        '''
        - It should be an inplace sort for self.testresults.
        - self.testresults is a list of (costs_i, vector_i) tuples
        - costs_i: list
        - vector_i: list
        - after sort:
            self.testresults[0] element has the lowest fitness
            self.testresults[-1] element has the highest fitness
        '''
        ...

    @abstractmethod
    def set_min_costs(self, key):
        ...

    @abstractmethod
    def set_max_costs(self, key):
        ...
        
    @abstractmethod
    def set_avg_costs(self, key):
        ...

    @abstractmethod
    def set_std_costs(self, key):
        ...

    @abstractmethod
    def set_min_vector(self, key):
        ...

    @abstractmethod
    def set_max_vector(self, key):
        ...


    def __call__(self):
        self.runtests()

class SingleObjAlgorithmEvaluation(AlgorithmEvaluation):
    pass


class MultiObjAlgorithmEvaluation(AlgorithmEvaluation):
    pass


if __name__=='__main__':
    # for testing
    from artap.algorithm_swarm import OMOPSO
    from artap.benchmark_functions import Ackley

    ef.testfactory.append(Ackley)

    test1 = SingleObjAlgorithmEvaluation(OMOPSO, 3)
    test1()
