from LexicalAnalyzer import TokenTypes
from .ExpressionNode import ExpressionNode
from .StatementsNode import StatementsNode
from .BinaryOperatorNode import BinaryOperatorNode
from LexicalAnalyzer import Token


class IfNode(ExpressionNode):
    """Класс узла операторов для  AST."""

    def __init__(
        self,
        then_node: StatementsNode,
        else_node: StatementsNode | None,
        condition_node: BinaryOperatorNode,
    ):
        self.then_node = then_node
        self.else_node = else_node
        self.condition_node = condition_node

    def __eq__(self, value):
        return (
            isinstance(value, IfNode)
            and self.then_node == value.then_node
            and self.condition_node == value.condition_node
        )

    def to_python(self, indent_level) -> str:
        python_code = indent_level * " " + f"if {self.condition_node.to_python(indent_level=0)}:\n"
        python_code += self.then_node.to_python(indent_level=indent_level + 4)
        if self.else_node:
            python_code = python_code + '\n' + indent_level * " " + "else:\n"
            python_code += self.else_node.to_python(indent_level=indent_level + 4)
        return python_code
