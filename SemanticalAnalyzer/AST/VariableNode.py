from .ExpressionNode import ExpressionNode
from LexicalAnalyzer import Token
from SemanticalAnalyzer import Variable


class VariableNode(ExpressionNode):
    """Класс для узла переменной."""

    def __init__(self, varibale: Variable, data_type):
        # TODO убрать data_type отсюда он и так в перемнной храниться
        # нахуй он еще и тут
        self.variable = varibale
        self.data_type = data_type

    def __eq__(self, value):
        return (
            isinstance(value, VariableNode)
            and self.variable == value.variable
            and self.data_type == value.data_type
        )

    def to_python(self, indent_level):
        return indent_level * " " + self.variable.name
