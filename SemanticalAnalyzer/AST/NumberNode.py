from .ExpressionNode import ExpressionNode
from LexicalAnalyzer import Token


class NumberNode(ExpressionNode):
    """Класс узла для числа."""

    def __init__(self, number: Token):
        self.number = number
