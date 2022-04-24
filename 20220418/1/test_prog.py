import unittest
import prog

class TestProg(unittest.TestCase):
    
    def testDAbove(self):
        self.assertEqual(prog.solveSquare(1, 0, -1), (1, -1))

    def testDBelow(self):
        self.assertEqual(prog.solveSquare(10, 2, 10), None)

    def testDEquals(self):
        self.assertEqual(prog.solveSquare(1, 2, 1), (-1, -1))
    
