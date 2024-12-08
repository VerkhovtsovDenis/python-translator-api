from .ExpressionNode import ExpressionNode
from LexicalAnalyzer import Token


class UnarOperatorNode(ExpressionNode):
    """Класс узла для унарного оператора."""

    def __init__(self, operator: Token, operand: Token):
        self.operator = operator
        self.operand = operand