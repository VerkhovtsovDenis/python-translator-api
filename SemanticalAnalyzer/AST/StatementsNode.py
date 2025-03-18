from .ExpressionNode import ExpressionNode


class StatementsNode(ExpressionNode):
    """Класс корневого узла AST."""

    def __init__(self):
        self.code_strings_nodes: list[ExpressionNode] = []

    def add_node(self, node: ExpressionNode):
        self.code_strings_nodes.append(node)

    def __eq__(self, value):
        return (
            isinstance(value, StatementsNode)
            and self.code_strings_nodes == value.code_strings_nodes
        )

    def to_python(self, indent_level=0) -> str:
        """
        Преобразует ноду дерева в питон.

        Raises:
            NotImplementedError: Метод не реализован.
        """

        return "\n".join(node.to_python(indent_level) for node in self.code_strings_nodes)
    
    def to_go(self, indent_level=0, variables = []) -> str:
        """
        Преобразует ноду дерева в го.

        Raises:
            NotImplementedError: Метод не реализован.
        """

        return "\n".join(node.to_go(indent_level, variables=variables) for node in self.code_strings_nodes)
