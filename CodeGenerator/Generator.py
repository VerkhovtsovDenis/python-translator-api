from SemanticalAnalyzer.AST import StatementsNode
from constants import SupportLanguages


class Generator:
    """Класс, отвечающий за герации кода по АСТ."""

    def __init__(self, ast: StatementsNode):
        self._ast = ast

    def generate(self, target_language: SupportLanguages) -> str:
        """
        Генерирует код на питон.

        Returns:
            str: Код на питон.
        """
        python_code = ""
        # TODO поолучать соотв метод генерации через getatr
        if target_language == SupportLanguages.PYTHON:
            for str_node in self._ast.code_strings_nodes:
                python_code += str_node.to_python()
                python_code += "\n"

        return python_code
