import unittest

from artap.problem import Problem
from artap.algorithm_nlopt import NLopt
from artap.algorithm_nlopt import GN_DIRECT_L
# from artap.algorithm_nlopt import GN_DIRECT_L_RAND
from artap.algorithm_nlopt import GN_MLSL
from artap.algorithm_nlopt import GN_CRS2_LM
from artap.algorithm_nlopt import GN_ISRES
from artap.algorithm_nlopt import GN_ESCH
from artap.algorithm_nlopt import LN_BOBYQA
from artap.algorithm_nlopt import LN_COBYLA
from artap.algorithm_nlopt import LN_NELDERMEAD
from artap.algorithm_nlopt import LN_SBPLX
from artap.algorithm_nlopt import LN_PRAXIS
from artap.algorithm_nlopt import LN_AUGLAG_EQ

from artap.results import Results
from artap.datastore import DummyDataStore
from artap.benchmark_functions import Booth
from agrossuite import agros as a2d


class MyProblem(Problem):
    """ Describe simple one objective optimization problem. """
    def __init__(self, name):
        parameters = {'x_1': {'initial_value': 2.5, 'bounds': [-10, 10]},
                      'x_2': {'initial_value': 1.5, 'bounds': [-10, 10]}}
        costs = ['F']

        super().__init__(name, parameters, costs)

    def evaluate(self, x):
        return [Booth.eval(x)]


class TestNLoptOptimization(unittest.TestCase):
    """ Tests simple one objective optimization problem."""

    def run_test(self, method, n_iterations=100):
        problem = MyProblem("NLopt_{}".format(method))
        algorithm = NLopt(problem)
        algorithm.options['verbose_level'] = 0
        algorithm.options['algorithm'] = method
        algorithm.options['xtol_abs'] = 1e-6
        algorithm.options['xtol_rel'] = 1e-3
        algorithm.options['ftol_rel'] = 1e-3
        algorithm.options['ftol_abs'] = 1e-6
        algorithm.options['n_iterations'] = n_iterations
        algorithm.run()

        results = Results(problem)
        optimum = results.find_minimum('F')
        self.assertAlmostEqual(optimum.costs[0], 0, places=1)

    def test_local_problem_nlopt_GN_DIRECT_L(self):
        self.run_test(GN_DIRECT_L, 400)

    # def test_local_problem_nlopt_GN_DIRECT_L_RAND(self):
    #    self.run_test(GN_DIRECT_L_RAND, 100)

    def test_local_problem_nlopt_GN_MLSL(self):
        self.run_test(GN_MLSL, 500)

    def test_local_problem_nlopt_GN_CRS2_LM(self):
        self.run_test(GN_CRS2_LM, 8000)

    def test_local_problem_nlopt_GN_ISRES(self):
        self.run_test(GN_ISRES, 6000)

    # def test_local_problem_nlopt_GN_ESCH(self):
    #     self.run_test(GN_ESCH, 5000)

    def test_local_problem_nlopt_LN_BOBYQA(self):
        self.run_test(LN_BOBYQA)

    def test_local_problem_nlopt_LN_COBYLA(self):
        self.run_test(LN_COBYLA)

    def test_local_problem_nlopt_LN_NELDERMEAD(self):
        self.run_test(LN_NELDERMEAD)

    def test_local_problem_nlopt_LN_SBPLX(self):
        self.run_test(LN_SBPLX, 200)

    def test_local_problem_nlopt_LN_AUGLAG_EQ(self):
        self.run_test(LN_AUGLAG_EQ)

    def test_local_problem_nlopt_LN_PRAXIS(self):
        self.run_test(LN_PRAXIS)


class ThisIsNotMyProblem(Problem):
    """
    There was a bug between the job queue and the nlopt --- this is a testproblem to test the interface between the
    agros and artap

    """
    def __init__(self, name):
        parameters = {'r1': {'initial_value': 0.02, 'bounds': [0.01, 0.03]},
                      'r2': {'initial_value': 0.04, 'bounds': [0.035, 0.1]}}
        costs = ['F1']
        self.C_req = 80.  # pF

        super().__init__(name, parameters, costs)

    def evaluate(self, x: list):
        # problem
        problem = a2d.problem(clear=True)
        problem.coordinate_type = "planar"
        problem.mesh_type = "triangle"

        # project parameters
        problem.parameters["r1"] = x[0]
        problem.parameters["r2"] = x[1]
        problem.parameters["eps"] = 2.5

        # fields
        # electrostatic
        electrostatic = problem.field("electrostatic")
        electrostatic.analysis_type = "steadystate"
        electrostatic.matrix_solver = "umfpack"
        electrostatic.number_of_refinements = 1
        electrostatic.polynomial_order = 2
        electrostatic.adaptivity_type = "disabled"
        electrostatic.solver = "linear"

        # boundaries
        electrostatic.add_boundary("GND", "electrostatic_potential", {"electrostatic_potential": 0})
        electrostatic.add_boundary("V", "electrostatic_potential", {"electrostatic_potential": 1})
        electrostatic.add_boundary("neumann", "electrostatic_surface_charge_density",
                                   {"electrostatic_surface_charge_density": 0})

        # materials
        electrostatic.add_material("dielectric",
                                   {"electrostatic_permittivity": "eps", "electrostatic_charge_density": 0})

        # geometry
        geometry = problem.geometry()
        geometry.add_edge("r1", 0, "r2", 0, boundaries={"electrostatic": "neumann"})
        geometry.add_edge("r2", 0, 0, "r2", angle=90, boundaries={"electrostatic": "GND"})
        geometry.add_edge(0, "r2", 0, "r1", boundaries={"electrostatic": "neumann"})
        geometry.add_edge("r1", 0, 0, "r1", angle=90, boundaries={"electrostatic": "V"})

        geometry.add_label("(r1 + r2) / 2.", "(r2 - r1) / 2", materials={"electrostatic": "dielectric"})

        computation = problem.computation()
        computation.solve()

        solution = computation.solution("electrostatic")
        result = solution.volume_integrals()["We"]

        C = 4 * 2 * result *1e12 # pF

        return [abs(C - self.C_req)]

class TestIsItNotMyProblem(unittest.TestCase):

    def test_run(self):

        problem = ThisIsNotMyProblem("AgrosProblem")
        algorithm = NLopt(problem)
        algorithm.options['n_iterations'] = 20
        algorithm.options['algorithm'] = LN_BOBYQA
        # algorithm.options['verbose_level'] = 2
        algorithm.run()

        results = Results(problem)
        optimum = results.find_minimum('F1')

        self.assertAlmostEqual(optimum.costs[0], 0, places=1)
        # tests that the optimal value is within the predefined boundaries
        # --- excludes possible errors between -> job -- nlopt and memory handling

        # r1 between the limits?
        self.assertTrue(optimum.vector[0]>=problem.parameters['r1']['bounds'][0])
        self.assertTrue(optimum.vector[0]<=problem.parameters['r1']['bounds'][1])

        # r2 between the limits?
        self.assertTrue(optimum.vector[1]>=problem.parameters['r2']['bounds'][0])
        self.assertTrue(optimum.vector[1]<=problem.parameters['r2']['bounds'][1])


if __name__ == '__main__':
    unittest.main()
