from typing import Any
from SemanticalAnalyzer.AST import VariableNode
from .ExpressionNode import ExpressionNode
from LexicalAnalyzer import Token
from SemanticalAnalyzer.Variable import BaseDataType, CharDataType, StringDataType


class ValueNode(ExpressionNode):
    """Класс узла для значения."""

    def __init__(self, value: Any, data_type: BaseDataType):
        self.value = value
        self.data_type = data_type

    def __eq__(self, value):
        return (
            isinstance(value, ValueNode)
            and self.value == value.value
            and self.data_type == value.data_type
        )

    def to_python(self, indent_level):
        if self.data_type not in (CharDataType, StringDataType):
            return str(self.value)
        else:
            return f"'{self.value}'"
