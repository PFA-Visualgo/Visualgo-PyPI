from .types import StaticVariables


class StaticAnalysisRes:
    pass


class StaticAnalysis:

    def analyse_code_types(self, code: str) -> StaticAnalysisRes:
        pass

    def get_code_variables(self, code: str) -> StaticVariables:
        """
        :demand: F.2.7
        """
        pass

    def get_code_functions_methods(self, code: str) -> list[str]:
        """
        :demand: F.2.8
        """
        pass
