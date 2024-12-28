from .ExpressionNode import ExpressionNode
from .StatementsNode import StatementsNode
from .BinaryOperatorNode import BinaryOperatorNode


class WhileNode(ExpressionNode):
    """Класс узла операторов для  AST."""

    def __init__(
        self,
        body_node: StatementsNode,
        condition_node: BinaryOperatorNode,
    ):
        self.body_node = body_node
        self.condition_node = condition_node

    def __eq__(self, value):
        return (
            isinstance(value, WhileNode)
            and self.body_node == value.body_node
            and self.condition_node == value.condition_node
        )

    def to_python(self, indent_level) -> str:
        indent = indent_level * " "
        python_code = indent + f"while {self.condition_node.to_python(indent_level=0)}:\n"

        if not self.body_node.code_strings_nodes:
            python_code += (" " * (indent_level + 4) + "pass")
        else:
            python_code += self.body_node.to_python(indent_level=indent_level + 4)
        return python_code
