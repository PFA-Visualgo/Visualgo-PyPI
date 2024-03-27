import unittest
import types

from visualgo.logic.static import StaticAnalyser, StaticAnalysisRes

code = """from visualgo.stuctures import *
x = 10
y = x
def foo():
    def bar():
        pass
    y = 20
    print(x)
    print(y)

foo()
my_tree = Tree()
obj.method()
"""

class TestStaticAnalyser(unittest.TestCase):

    def test_analyse_code_types(self):
        global code
        res = StaticAnalyser.analyse_code_types(code)
        assert ('x', 0) in res.variables
        assert ('y', 0) in res.variables
        assert ('y', 1) in res.variables
        assert ('my_tree', 0) in res.variables
        assert len(res.variables) == 4

        assert 'Tree' in res.visualgo_types
        assert len(res.visualgo_types) == 1

        assert ('foo', 0) in res.user_functions
        assert ('bar', 1) in res.user_functions
        assert len(res.user_functions) == 2

        assert 'method' in res.functions_calls
        assert 'print' in res.functions_calls
        assert 'foo' in res.functions_calls
        assert len(res.functions_calls) == 3


if __name__ == "__main__":
    import pytest
    pytest.main([__file__])