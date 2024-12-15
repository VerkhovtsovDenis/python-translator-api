class ExpressionNode:
    """базовый класс для всех узлов AST."""

    def to_python(self) -> str:
        """
        Преобразует ноду дерева в питон.

        Raises:
            NotImplementedError: Метод не реализован.
        """
        raise NotImplementedError()
