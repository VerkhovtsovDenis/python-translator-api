from .ExpressionNode import ExpressionNode
from LexicalAnalyzer import Token


class BinaryOperatorNode(ExpressionNode):
    """Класс узла для бинарного оператора."""

    def __init__(self, operator: Token, left_operand: Token, right_operand: Token):
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand
