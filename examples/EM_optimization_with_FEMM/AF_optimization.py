""" Example shows how to use Artap together with locally installed FEMM """

import os
from artap.executor import LocalFEMMExecutor
from artap.problem import Problem
from artap.algorithm_scipy import ScipyOpt
from artap.results import Results
from artap.algorithm_genetic import NSGAII, EpsMOEA


class FEMMProblem(Problem):
    """ Describe simple one objective optimization problem."""

    def set(self):
        self.name = "FEMMProblem"

        # Parameters must be defined in the FEMM model
        # pp = 0.8 -- relative pole pitch: 0.4 - 0.99
        # p_offset = 0.8 -- relative offset: 0 - 0.99
        self.parameters = [{'name': 'pp', 'initial_value': 0.8, 'bounds': [0.5, 0.9]},
                           {'name': 'p_offset', 'initial_value': 0.8, 'bounds': [0.5, 0.9]}]

        self.costs = [{'name': 'F1', 'criteria': 'minimize'}]
        self.output_files = ["output.txt"]

        # Executor serves for calling the FEMM
        self.executor = LocalFEMMExecutor(self,
                                          script_file="AF_OpenCircuitAnalysisParametric.lua",
                                          output_files=["output.txt"])

    # Calculate the value of the objective function
    def evaluate(self, individual):
        cog = self.executor.eval(individual)[0]  # method evaluate must return list
        if cog < 1.:
            cog = 1e10
        return [cog]

    # This method processes files generated by 3rd party software, depends on files format
    def parse_results(self, output_files, individual):
        with open(output_files[0]) as file:
            content = file.readlines()
            content = content[0]
            content = content.split(',')
            content = [float(i) for i in content[:-1]]
            cogging_torque = max(content) - min(content)
            print('cogging:', cogging_torque)
        # return [float(content[0])]
        return [cogging_torque]


problem = FEMMProblem()        # Creating problem
#algorithm = ScipyOpt(problem)  # Algorithm from Scipy was choosen
#algorithm.options['algorithm'] = 'COBYLA'
#algorithm.options['n_iterations'] = 5
#algorithm.run()

algorithm  = NSGAII(problem)
#algorithm = EpsMOEA(problem)
#algorithm = SMPSO(problem)
algorithm.options['max_population_number'] = 5
algorithm.options['max_population_size'] = 4
algorithm.run()


# Post - processing the results
results = Results(problem)

res_individual = results.find_optimum()
print(res_individual.vector)
for i in range(len(problem.parameters)):
    print("{} : {}".format(problem.parameters[i].get("name"), res_individual.vector[i]))
