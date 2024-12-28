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
        if target_language == SupportLanguages.PYTHON:
            return self._ast.to_python()
