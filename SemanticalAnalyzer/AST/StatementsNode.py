from .ExpressionNode import ExpressionNode


class StatementsNode(ExpressionNode):
    """Класс корневого узла AST."""

    def __init__(self):
        self.code_strings: list[ExpressionNode] = []

    def add_node(self, node: ExpressionNode):
        self.code_strings.append(node)

    def __eq__(self, value):
        return (
            isinstance(value, StatementsNode)
            and self.code_strings == value.code_strings
        )
