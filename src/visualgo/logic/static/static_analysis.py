from .types import StaticVars


class StaticAnalysisRes:
    pass


class StaticAnalysis:

    def analyse_code_types(self, code: str) -> StaticAnalysisRes:
        pass

    def get_code_variables(self, code: str) -> StaticVars:
        pass

    def get_code_functions_methods(self, code: str) -> list[str]:
        pass
