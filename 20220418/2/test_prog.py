import unittest
from unittest.mock import Mock, MagicMock
import prog

class TestProg(unittest.TestCase):
        def testDAbove(self):
            values = {"a": 1, "b": 0, "c": -1}
            def side_effects(name):
                return values[name]
            prog.SquareIO.inputCoeff = MagicMock(side_effect=side_effects)
            Io = prog.SquareIO()
            a = Io.inputCoeff("a")
            b = Io.inputCoeff("b")
            c = Io.inputCoeff("c")
            self.assertEqual(prog.solveSquare(a, b, c), (1, -1))
        
        def testDBelow(self):
            values = {"a": 10, "b": 2, "c": 10}
            def side_effects(name):
                return values[name]
            prog.SquareIO.inputCoeff = MagicMock(side_effect=side_effects)
            Io = prog.SquareIO()
            a = Io.inputCoeff("a")
            b = Io.inputCoeff("b")
            c = Io.inputCoeff("c")
            self.assertEqual(prog.solveSquare(10, 2, 10), None)


        def testDEquals(self):
            values = {"a": 1, "b": 2, "c": 1}
            def side_effects(name):
                return values[name]
            prog.SquareIO.inputCoeff = MagicMock(side_effect=side_effects)
            Io = prog.SquareIO()
            a = Io.inputCoeff("a")
            b = Io.inputCoeff("b")
            c = Io.inputCoeff("c")
            self.assertEqual(prog.solveSquare(1, 2, 1), (-1, -1))