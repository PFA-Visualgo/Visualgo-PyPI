import ast
from dataclasses import dataclass

from .types import StaticVariables

@dataclass
class StaticAnalysisRes:
    variables: list[dict[str, int]]
    visualgo_types: list[dict[str, None]]
    user_functions: list[dict[str, int]]
    functions_calls: list[dict[str, None]]



class StaticAnalyser:
    _visualgo_types = {"Tree", 
                  "Graph", 
                  "List", 
                  "Queue",
                  "Stack", 
                  "Heap", 
                  "PriorityQueue", 
                  "HashTable", 
                  "BinarySearchTree"}
    
    @classmethod
    def analyse_code_types(cls, code: str) -> StaticAnalysisRes:
        tree = ast.parse(code)

        variables = []
        functions = []
        method_calls = []

        def traverse(node, level=-1):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        variables.append((target.id, level))
            elif isinstance(node, ast.FunctionDef):
                functions.append((node.name, level))
            elif isinstance(node, ast.Call):
                if isinstance(node.func, ast.Attribute):
                    # Method call
                    method_calls.append((node.func.attr, None))
                elif isinstance(node.func, ast.Name):
                    # Function call
                    method_calls.append((node.func.id, None))

            for child_node in ast.iter_child_nodes(node):
                traverse(child_node, level + 1)

        traverse(tree)

        visualgo_types = []

        functions_calls = []

        for method_call, _ in method_calls:
            if method_call in cls._visualgo_types:
                visualgo_types.append(method_call)
            elif method_call not in functions_calls:
                functions_calls.append(method_call)

        return StaticAnalysisRes(variables, visualgo_types, functions, functions_calls)

    @classmethod
    def get_code_variables(cls, code: str) -> StaticVariables:
        """
        :demand: F.2.7
        """
        pass

    @classmethod
    def get_code_functions_methods(cls, code: str) -> list[str]:
        """
        :demand: F.2.8
        """
        pass
