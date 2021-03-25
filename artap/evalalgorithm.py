from abc import abstractmethod
from artap.results import Results
from artap.algorithm import Algorithm
from artap import evalfunctions as ef
import statistics
import json
import time


'''
TODO:
    - tests
    - abstracting
    - kwargs
    - min,max,avg,std / dimension for vectors
    - investigate memory leak
'''


class AlgorithmEvaluation:

    def __init__(self, algorithm: Algorithm, dimension=3, **kwargs):
        self.dimension = dimension
        self.set_dimension(self.dimension)
        self.algorithm = algorithm

        self.results = {}
        self.testresults = list()
        self.times = list()

        self.cfg = {
                'algorithm': str(self.algorithm.__name__),
                'nb_dimension': self.dimension,
                'nb_testrun': kwargs.pop("nb_testrun", 50),
                'nb_iteration': kwargs.pop("nb_iter", 30),
                'nb_individual': kwargs.pop("nb_individual", 100)
                }

    def runtests(self):
        self.results.clear()
        self.set_dimension(self.dimension)

        #while test := ef.testfactory.pop():
        for test in ef.testfactory:
            self.testresults.clear()
            self.times.clear()
            for i in range(self.cfg['nb_testrun']):
                print(i, end=' ')
                problem = test(dimension=self.dimension)
                alg = self.algorithm(problem)
                problem.logger.disabled = True
                alg.options['n_iterations'] = self.cfg['nb_iteration']
                alg.options['max_population_size'] = self.cfg['nb_individual']
                alg.options['max_processes'] = 1
                t0 = time.process_time()
                alg.run()
                self.times.append(time.process_time() - t0)
                self.testresults.append(self.get_results(problem))
                
                # temp. solution 4 memory leak
                alg.problem.individuals.clear()
                problem.individuals.clear()


            key = str(problem.name)
            self.results.setdefault(key, {})
            self.sort_testresults() # !!!!!!!

            # statistics
            self.set_time_stats(key)

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
            #print(self.results[key])
            print()

        #cleanup
        self.testresults.clear()
        del problem

    def set_dimension(self, dim):
        ef.TestFunctionBase.dimension = dim


    def get_results(self, problem):
        res = Results(problem).find_optimum()
        c = list(res.costs)
        v = list(res.vector)
        return c, v

    def costs_getter(self, idx):
        return self.testresults[idx][0]

    def vector_getter(self, idx):
        return self.testresults[idx][1]

    def to_dict(self):
        self.results['metadata'] = self.cfg.copy()
        print(json.dumps(self.results, indent=2))

        # for testing only
        with open('res.json', 'w') as f:
            json.dump(self.results, f, indent=4)
        
        return self.results.copy()

    def set_time_stats(self, key):
        maxt = max(self.times)
        mint = min(self.times)
        stdt = statistics.stdev(self.times)
        avgt = statistics.fmean(self.times)
        self.results[key]['times'] = {
                'fastest': mint,
                'slowest': maxt,
                'average': avgt,
                'stddev': stdt
                }

    @abstractmethod
    def sort_testresults(self):
        '''
        - It should be an inplace sort for self.testresults.
        - self.testresults is a list of (costs_i, vector_i) tuples
        - costs_i: list
        - vector_i: list
        - after sort:
            self.testresults[0] element is the "best"
            self.testresults[-1] element is the "worst"
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

    def sort_testresults(self):
        self.testresults.sort(key=lambda li: li[0][0])

    def set_min_costs(self, key):
        self.results[key]['min_costs'] = self.costs_getter(0)

    def set_max_costs(self, key):
        self.results[key]['max_costs'] = self.costs_getter(-1)

    def set_avg_costs(self, key):
        c = (self.costs_getter(i)[0] for i in range(len(self.testresults)))
        avg = statistics.fmean(c)
        self.results[key]['avg_costs'] = avg

    def set_std_costs(self, key):
        c = (self.costs_getter(i)[0] for i in range(len(self.testresults)))
        std = statistics.stdev(c)
        self.results[key]['std_costs'] = std

    def set_min_vector(self, key):
        self.results[key]['min_vector'] = self.vector_getter(0)

    def set_max_vector(self, key):
        self.results[key]['max_vector'] = self.vector_getter(-1)






class MultiObjAlgorithmEvaluation(AlgorithmEvaluation):
    pass


if __name__=='__main__':
    # for testing
    from artap.algorithm_swarm import OMOPSO, SMPSO
    from artap.benchmark_functions import Ackley
    
    #ef.testfactory.clear()
    #ef.register('F1', (-100.0, 100.0))(ef.f1)
    #ef.register('F2', (-100.0, 100.0))(ef.f2)
    ef.testfactory.append(Ackley)

    test1 = SingleObjAlgorithmEvaluation(OMOPSO, 3)
    test1()
    test1.to_dict()


'''
EXAMPLE OUTPUT
{
    "F1": {
        "times": {
            "fastest": 0.671875,
            "slowest": 0.90625,
            "average": 0.760625,
            "stddev": 0.04676219419704821
        },
        "min_costs": [
            0.0
        ],
        "max_costs": [
            2.620765167333719e-06
        ],
        "avg_costs": 1.7034246947777588e-07,
        "std_costs": 4.155960410201102e-07,
        "min_vector": [
            0.0,
            0.0,
            0.0
        ],
        "max_vector": [
            0.000331418438636243,
            -0.001097253554089737,
            -0.0011432242229340115
        ]
    },
    "F2": {
        "times": {
            "fastest": 0.75,
            "slowest": 1.703125,
            "average": 0.9653125,
            "stddev": 0.1918939343679051
        },
        "min_costs": [
            0.0
        ],
        "max_costs": [
            0.023686068691330265
        ],
        "avg_costs": 0.0011259507304003972,
        "std_costs": 0.003486020439012218,
        "min_vector": [
            0.0,
            0.0,
            0.0
        ],
        "max_vector": [
            -0.09672838599165612,
            0.0007603351540788408,
            -3.5357524136544944e-05
        ]
    },
    "F3": {
        "times": {
            "fastest": 0.765625,
            "slowest": 1.671875,
            "average": 0.8865625,
            "stddev": 0.14423892286280582
        },
        "min_costs": [
            0.0
        ],
        "max_costs": [
            9.67167587879903e-06
        ],
        "avg_costs": 4.481571591818625e-07,
        "std_costs": 1.439959235935891e-06,
        "min_vector": [
            0.0,
            0.0,
            0.0
        ],
        "max_vector": [
            0.0023734777181962778,
            0.0010622439719452162,
            -0.0007706176934029226
        ]
    },
    "F4": {
        "times": {
            "fastest": 0.765625,
            "slowest": 1.03125,
            "average": 0.85125,
            "stddev": 0.05932966851691092
        },
        "min_costs": [
            0.0
        ],
        "max_costs": [
            1.2584590307682126e-09
        ],
        "avg_costs": 6.243708089058863e-11,
        "std_costs": 2.1934035365829676e-10,
        "min_vector": [
            0.0,
            0.0,
            0.0
        ],
        "max_vector": [
            7.582024055706024e-10,
            0.0,
            -0.0007938362917956788
        ]
    },
    "F5": {
        "times": {
            "fastest": 0.734375,
            "slowest": 2.09375,
            "average": 0.9125,
            "stddev": 0.259946429184781
        },
        "min_costs": [
            4.031462359277374e-05
        ],
        "max_costs": [
            0.0017415251597531017
        ],
        "avg_costs": 0.0006765395110381534,
        "std_costs": 0.000466396446778928,
        "min_vector": [
            -0.493693242589328,
            -0.4992657573349901,
            -0.4999820482706449
        ],
        "max_vector": [
            -0.5255485721694763,
            -0.5276201980816806,
            -0.48194673775233704
        ]
    },
    "F6": {
        "times": {
            "fastest": 0.734375,
            "slowest": 1.65625,
            "average": 0.889375,
            "stddev": 0.13369920836088198
        },
        "min_costs": [
            4.440892098500626e-16
        ],
        "max_costs": [
            2.138976349375099e-06
        ],
        "avg_costs": 4.879650832734228e-08,
        "std_costs": 3.019504448017135e-07,
        "min_vector": [
            0.0,
            0.0,
            0.0
        ],
        "max_vector": [
            0.00015137388343575313,
            -0.00010949534756584262,
            -0.000266482669427421
        ]
    },
    "F7": {
        "times": {
            "fastest": 0.734375,
            "slowest": 1.5625,
            "average": 0.86625,
            "stddev": 0.14341965147277214
        },
        "min_costs": [
            0.00015651693699965844
        ],
        "max_costs": [
            0.3603715876100994
        ],
        "avg_costs": 0.049741718548322815,
        "std_costs": 0.08196649416819003,
        "min_vector": [
            1.0668237264083973,
            1.0680435101164676,
            1.0677654866003348
        ],
        "max_vector": [
            1.7070134269132105,
            1.765905055922064,
            1.7571015406884563
        ]
    },
    "F8": {
        "times": {
            "fastest": 0.734375,
            "slowest": 0.96875,
            "average": 0.8209375,
            "stddev": 0.05265302800806775
        },
        "min_costs": [
            0.0
        ],
        "max_costs": [
            2.1595134569452057e-09
        ],
        "avg_costs": 6.922398654296558e-11,
        "std_costs": 3.3553553972483795e-10,
        "min_vector": [
            0.0,
            0.0,
            0.0
        ],
        "max_vector": [
            1.1347447872877662e-08,
            0.0,
            3.2992349592737238e-06
        ]
    },
    "F9": {
        "times": {
            "fastest": 0.71875,
            "slowest": 1.359375,
            "average": 0.898125,
            "stddev": 0.1305084127204692
        },
        "min_costs": [
            0.0
        ],
        "max_costs": [
            1.391939008499321e-09
        ],
        "avg_costs": 5.62804203241285e-11,
        "std_costs": 2.391860470529376e-10,
        "min_vector": [
            0.0,
            0.0,
            0.0
        ],
        "max_vector": [
            2.124131090771228e-06,
            -1.5824550851354364e-06,
            0.0
        ]
    },
    "F10": {
        "times": {
            "fastest": 0.703125,
            "slowest": 1.109375,
            "average": 0.8446875,
            "stddev": 0.08378181032343135
        },
        "min_costs": [
            -78.32410258627597
        ],
        "max_costs": [
            -77.92075553024195
        ],
        "avg_costs": -78.1660630162717,
        "std_costs": 0.1031361007637868,
        "min_vector": [
            -2.884265215899486,
            -2.8994960852864406,
            -2.88534952759778
        ],
        "max_vector": [
            -2.790683796202795,
            -2.987247035769242,
            -2.773249411058594
        ]
    },
    "F11": {
        "times": {
            "fastest": 0.703125,
            "slowest": 1.140625,
            "average": 0.825,
            "stddev": 0.08249874380614433
        },
        "min_costs": [
            0.0
        ],
        "max_costs": [
            1.3972414637897917e-05
        ],
        "avg_costs": 2.8713398733190315e-07,
        "std_costs": 1.9752591999035384e-06,
        "min_vector": [
            0.0,
            0.0,
            0.0
        ],
        "max_vector": [
            -0.10030741981716909,
            0.0,
            0.0
        ]
    },
    "F12": {
        "times": {
            "fastest": 0.6875,
            "slowest": 0.984375,
            "average": 0.8415625,
            "stddev": 0.07770999467046484
        },
        "min_costs": [
            0.00012922939866232935
        ],
        "max_costs": [
            0.012994957329241164
        ],
        "avg_costs": 0.0025670891994046857,
        "std_costs": 0.0023050037917180842,
        "min_vector": [
            0.9990723303851169,
            0.9930456147186708,
            0.9910978836748614
        ],
        "max_vector": [
            1.0301732274771014,
            0.9143074662129378,
            1.0325760966446471
        ]
    },
    "FMultiobj": {
        "times": {
            "fastest": 0.71875,
            "slowest": 1.0625,
            "average": 0.8934375,
            "stddev": 0.07063524284581851
        },
        "min_costs": [
            0.0,
            -0.1388522196939349
        ],
        "max_costs": [
            0.0,
            -0.9875119705897072
        ],
        "avg_costs": 0.0,
        "std_costs": 0.0,
        "min_vector": [
            -1.0,
            -0.759474180799368,
            -0.5842531520370684
        ],
        "max_vector": [
            -1.0,
            -0.6248935019205872,
            -0.24342817501346684
        ]
    },
    "Ackley function": {
        "times": {
            "fastest": 0.90625,
            "slowest": 1.203125,
            "average": 1.0025,
            "stddev": 0.07173205617193097
        },
        "min_costs": [
            4.440892098500626e-16
        ],
        "max_costs": [
            0.0001700919415914548
        ],
        "avg_costs": 3.099206356170115e-05,
        "std_costs": 3.72723065188522e-05,
        "min_vector": [
            0.0,
            0.0,
            0.0
        ],
        "max_vector": [
            -7.259434433103121e-05,
            7.4319495111946216e-06,
            -9.659526623136453e-06
        ]
    },
    "metadata": {
        "algorithm": "OMOPSO",
        "nb_dimension": 3,
        "nb_testrun": 50,
        "nb_iteration": 30,
        "nb_individual": 100
    }
}
'''
