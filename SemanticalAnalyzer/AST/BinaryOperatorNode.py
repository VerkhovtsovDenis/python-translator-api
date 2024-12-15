from .ExpressionNode import ExpressionNode
from LexicalAnalyzer import Token


class BinaryOperatorNode(ExpressionNode):
    """Класс узла для бинарного оператора."""

    def __init__(
        self,
        operator: Token,
        left_operand: ExpressionNode,
        right_operand: ExpressionNode,
    ):
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand

    def __eq__(self, value):
        return (
            isinstance(value, BinaryOperatorNode)
            and self.operator == value.operator
            and self.left_operand == value.left_operand
            and self.right_operand == value.right_operand
        )
