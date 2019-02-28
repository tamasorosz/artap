import unittest
from artap.doe import build_box_behnken, build_lhs, build_frac_fact, build_full_fact, build_plackett_burman
from artap.individual import Individual
from artap.operators import FullFactorGeneration, PlackettBurmanGeneration, BoxBehnkenGeneration, LHSGeneration


class TestDOE(unittest.TestCase):

    def setUp(self):
        self.parameters = {'x_1': {'initial_value': 2.5, 'bounds': [-2.5, 5]},
                           'x_2': {'initial_value': 1.5, 'bounds': [1, 3.4]},
                           'x_3': {'initial_value': 3.5, 'bounds': [6, 10]}}

    # Factorial Designs
    def test_full_fact_generator(self):
        # General Full-Factorial
        gen = FullFactorGeneration(self.parameters)
        individuals = gen.generate(center=False)

        # size
        self.assertEqual(len(individuals), 8)
        # values
        self.assertEqual(individuals[0].vector[0], -2.5)
        self.assertEqual(individuals[1].vector[0], 5.0)
        self.assertEqual(individuals[2].vector[1], 3.4)
        self.assertEqual(individuals[3].vector[1], 3.4)
        self.assertEqual(individuals[7].vector[2], 10.0)

        gen = FullFactorGeneration(self.parameters)
        individuals = gen.generate(center=True)

        self.assertEqual(individuals[3].vector[0], -2.5)
        self.assertEqual(individuals[-1].vector[1], 3.4)

    def test_plackett_burman_generator(self):
        # Plackett-Burman
        gen = PlackettBurmanGeneration(self.parameters)
        individuals = gen.generate()

        # size
        self.assertEqual(len(individuals), 4)
        # values
        self.assertEqual(individuals[0].vector[0], -2.5)
        self.assertEqual(individuals[1].vector[0], 5.0)
        self.assertEqual(individuals[2].vector[2], 6.0)
        self.assertEqual(individuals[3].vector[1], 3.4)

    # Response - Surface Designs
    def test_box_behnken_generator(self):
        # Box-Behnken
        gen = BoxBehnkenGeneration(self.parameters)
        individuals = gen.generate()

        # size
        self.assertEqual(len(individuals), 13)
        # values
        self.assertEqual(individuals[2].vector[2], 8.0)
        self.assertEqual(individuals[3].vector[1], 3.4)
        self.assertEqual(individuals[5].vector[0], 5.0)
        self.assertEqual(individuals[12].vector[1], 2.2)

    # Randomized Designs
    def test_lhs_generation(self):
        # Latin - Hypercube
        gen = LHSGeneration(self.parameters)
        individuals = gen.generate(number=3)

        # size
        self.assertEqual(len(individuals), 3)
        # values
        self.assertTrue(self.parameters['x_1']['bounds'][0] <= individuals[0].vector[0] <= self.parameters['x_1']['bounds'][1] and
                        self.parameters['x_2']['bounds'][0] <= individuals[0].vector[1] <= self.parameters['x_2']['bounds'][1] and
                        self.parameters['x_3']['bounds'][0] <= individuals[0].vector[2] <= self.parameters['x_3']['bounds'][1] and
                        self.parameters['x_1']['bounds'][0] <= individuals[1].vector[0] <= self.parameters['x_1']['bounds'][1] and
                        self.parameters['x_2']['bounds'][0] <= individuals[1].vector[1] <= self.parameters['x_2']['bounds'][1] and
                        self.parameters['x_3']['bounds'][0] <= individuals[1].vector[2] <= self.parameters['x_3']['bounds'][1] and
                        self.parameters['x_1']['bounds'][0] <= individuals[2].vector[0] <= self.parameters['x_1']['bounds'][1] and
                        self.parameters['x_2']['bounds'][0] <= individuals[2].vector[1] <= self.parameters['x_2']['bounds'][1] and
                        self.parameters['x_3']['bounds'][0] <= individuals[2].vector[2] <= self.parameters['x_3']['bounds'][1])


if __name__ == '__main__':
    unittest.main()
