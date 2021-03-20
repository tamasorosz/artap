import unittest
import artap.evalfunctions as ef 
from artap.individual import Individual

PLACES = 7

class TestOptimums(unittest.TestCase):
    def test_optimum_f1(self):
        opt = Individual([0,0,0])
        tf = ef.TestFunctionF1()
        for xi in tf.evaluate(opt):
            self.assertAlmostEqual(xi, 0, places=PLACES)

    def test_optimum_f2(self):
        opt = Individual([0,0,0])
        tf = ef.TestFunctionF2()
        for xi in tf.evaluate(opt):
            self.assertAlmostEqual(xi, 0, places=PLACES)

    def test_optimum_f3(self):
        opt = Individual([0,0,0])
        tf = ef.TestFunctionF3()
        for xi in tf.evaluate(opt):
            self.assertAlmostEqual(xi, 0 , places=PLACES)

    def test_optimum_f4(self):
        opt = Individual([0,0,0])
        tf = ef.TestFunctionF4()
        for xi in tf.evaluate(opt):
            self.assertAlmostEqual(xi, 0, places=PLACES)
   
    def test_optimum_f5(self):
        opt = Individual([-0.5, -0.5, -0.5])
        tf = ef.TestFunctionF5()
        for xi in tf.evaluate(opt):
            self.assertAlmostEqual(xi, 0, places=PLACES)
   
    def test_optimum_f6(self):
        opt = Individual([0, 0, 0])
        tf = ef.TestFunctionF6()
        for xi in tf.evaluate(opt):
            self.assertAlmostEqual(xi, 0.0, places=PLACES)

    def test_optimum_f7(self):
        opt = Individual([1, 1, 1])
        tf = ef.TestFunctionF7()
        for xi in tf.evaluate(opt):
            self.assertAlmostEqual(xi, 0, places=PLACES)

    def test_optimum_f8(self):
        opt = Individual([0, 0, 0])
        tf = ef.TestFunctionF8()
        for xi in tf.evaluate(opt):
            self.assertAlmostEqual(xi, 0, places=PLACES)

    def test_optimum_f9(self):
        opt = Individual([0, 0, 0])
        tf = ef.TestFunctionF9()
        for xi in tf.evaluate(opt):
            self.assertAlmostEqual(xi, 0, places=PLACES)
    
    def test_optimum_f10(self):
        opt = Individual([-3, -3, -3])
        tf = ef.TestFunctionF10()
        for xi in tf.evaluate(opt):
            self.assertAlmostEqual(xi, -78, places=PLACES)
    
    def test_optimum_f11(self):
        opt = Individual([0, 0, 0])
        tf = ef.TestFunctionF11()
        for xi in tf.evaluate(opt):
            self.assertAlmostEqual(xi, 0, places=PLACES)
    
    def test_optimum_f12(self):
        opt = Individual([1, 1, 1])
        tf = ef.TestFunctionF12()
        for xi in tf.evaluate(opt):
            self.assertAlmostEqual(xi, 0, places=PLACES)

if __name__ == '__main__':
    unittest.main()


