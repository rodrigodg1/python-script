#arquivo a ser executado para os testes

import unittest
import aritimetic

class Test_sub(unittest.TestCase):
    def test_sub_int(self):
        sub = aritimetic.sub(50,50)
        self.assertEqual(sub,0)
    def test_sub_float(self):
        sub = aritimetic.sub(2.5,2.5)
        self.assertEqual(sub,0.0)



if __name__ == '__main__':
    unittest.main()