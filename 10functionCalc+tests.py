class Calculator(object):

    def addition(self, x, y):
        return x+y   

    def substract(self, x, y):
        return x-y 

    def multiply(self, x, y):
        return x*y

    def div(self, x, y):
        return x/y

    def sqroot(self, x):
        return x**0.5

    def sqpower(self, x):
        return x*x

    def cubepower(self, x):
        return x*x*x    

    from math import sin
    print sin(1)

    from math import cos
    print cos(1)

    from math import tan
    print tan(1)


import unittest
class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()
    def test_calculator_addition_method_connect_result(self):
        result=self.calc.addition(2,2)
        self.assertEqual(4, result)
        result=self.calc.addition(2,4)
        self.assertEqual(6, result)
    
    def test_calculator_substract_method_connect_result(self):
        result=self.calc.substract(3,2)
        self.assertEqual(1, result)
        result=self.calc.substract(8,4)
        self.assertEqual(4, result)
        
    def test_calculator_multiply_method_connect_result(self):
        result=self.calc.multiply(2,2)
        self.assertEqual(4, result)
        result=self.calc.multiply(6,7)
        self.assertEqual(42, result)

    def test_calculator_div_method_connect_result(self):
        result=self.calc.div(49, 7)
        self.assertEqual(7, result)
        result=self.calc.div(56, 8)
        self.assertEqual(7, result)

    def test_calculator_sqroot_method_connect_result(self):
        result=self.calc.sqroot(4)
        self.assertEqual(2, result)
        result=self.calc.sqroot(9)
        self.assertEqual(3, result)

    def test_calculator_sqpower_method_connect_result(self):
        result=self.calc.sqpower(5)
        self.assertEqual(25, result)
        result=self.calc.sqpower(3)
        self.assertEqual(9, result)

    def test_calculator_cubepower_method_connect_result(self):
        result=self.calc.cubepower(3)
        self.assertEqual(27, result)
        result=self.calc.cubepower(2)
        self.assertEqual(8, result)
    
def main():
    unittest.main()          
if __name__=='__main__':
    unittest.main()
