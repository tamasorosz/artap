from unittest import TestCase, main
from context import RemoteExecutor
from context import Problem   
from context import ScipyNelderMead
from scipy.optimize import minimize
import os
import getpass

class TestProblem(Problem):
    """ Describe simple one obejctive optimization problem. """
    def __init__(self, name):        
        self.max_population_number = 1
        self.max_population_size = 1
        self.parameters = {'x_1': {'initial_value':10}, 
                           'x_2': {'initial_value':10}}
        self.costs = ['F1']
        # current username
        user = getpass.getuser()
        self.executor = RemoteExecutor(username=user)

        cwd = os.getcwd()
        self.executor.script = cwd + "/tests/test_remote_eval.py"
        
        super().__init__(name, self.parameters, self.costs)

    def eval(self, x):
        result = self.executor.eval(x)

        print(result)
        return result
        
class TestRemoteOptimization(TestCase):
    """ Tests simple optimization problem where calculation of 
        goal function is performed on remote machine.
    """
    def test_remote_run(self):        
        """ Tests one calculation of goal function."""
        problem = TestProblem("RemotePythonProblem")        
        problem.eval([1, 1])
        # problem.read_from_database()
        # optimum = problem.data[-1][-1]
        # self.assertAlmostEqual(optimum, 0)
    
    def test_remote_optimization(self):        
        """ Tests simple optimization problem. """ 
        problem = TestProblem("RemotePythonProblem")
        algorithm = ScipyNelderMead(problem)
        algorithm.run()  
        problem.read_from_database()
        optimum = problem.data[-1][-1] # Takes last individual

        self.assertAlmostEqual(optimum, 0)

if __name__ == '__main__':
    main()