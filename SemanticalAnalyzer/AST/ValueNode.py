from SemanticalAnalyzer.AST import VariableNode
from .ExpressionNode import ExpressionNode
from LexicalAnalyzer import Token
from SemanticalAnalyzer.Variable import BaseDataType


class ValueNode(ExpressionNode):
    """Класс узла для значения."""

    def __init__(self, token: Token, data_type: BaseDataType):
        self.variable = token
        self.data_type = data_type

    def __eq__(self, value):
        return (
            isinstance(value, ValueNode)
            and self.variable == value.variable
            and self.data_type == value.data_type
        )

    def to_python(self):
        return self.variable.value
