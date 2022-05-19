import unittest
from prog import solve

class TestSolve(unittest.TestCase):
    def test_correct_solution(self):
        assert solve(1, 1) == -1
    
    def test_no_solution(self):
        assert solve(0, 0) is None