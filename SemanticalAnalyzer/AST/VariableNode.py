from .ExpressionNode import ExpressionNode
from LexicalAnalyzer import Token


class VariableNode(ExpressionNode):
    """Класс для узла переменной."""

    def __init__(self, token: Token, data_type):
        self.variable = token
        self.data_type = data_type

    def __eq__(self, value):
        return (
            isinstance(value, VariableNode)
            and self.variable == value.variable
            and self.data_type == value.data_type
        )

    def to_python(self):
        return self.variable.value
