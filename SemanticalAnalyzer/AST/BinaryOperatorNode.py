from .ExpressionNode import ExpressionNode
from LexicalAnalyzer import Token, TokenTypes
from SemanticalAnalyzer.Variable import DATA_TYPES_TO_PYTHON


class BinaryOperatorNode(ExpressionNode):
    """Класс узла для бинарного оператора."""

    def __init__(
        self,
        operator: Token,
        left_operand: ExpressionNode,
        right_operand: ExpressionNode,
        brackets: bool = False,
        type_hint: bool = False,
    ):
        self.operator = operator
        self.left_operand = left_operand
        self.right_operand = right_operand
        self.brackets = brackets
        self.type_hint = type_hint

    def __eq__(self, value):
        return (
            isinstance(value, BinaryOperatorNode)
            and self.operator == value.operator
            and self.left_operand == value.left_operand
            and self.right_operand == value.right_operand
        )

    OPERATOR_TOKEN_TYPES_TO_PYTHON = {
        TokenTypes.PLUS: "+",
        TokenTypes.MINUS: "-",
        TokenTypes.MULTIPLY: "*",
        TokenTypes.DIVISION: "/",
        TokenTypes.DIV: "//",
        TokenTypes.MOD: "%",
        TokenTypes.ASSIGNMENT: "=",
    }

    def to_python(self) -> str:
        """
        Преобразует ноду дерева в питон.

        Raises:
            NotImplementedError: Метод не реализован.
        """
        left_bracket, right_bracket = "", ""
        if self.brackets:
            left_bracket, right_bracket = "(", ")"

        type_hint = ""
        if self.operator.token_type == TokenTypes.ASSIGNMENT and self.type_hint:
            type_hint = f": {DATA_TYPES_TO_PYTHON[self.left_operand.data_type]}"

        return (
            left_bracket
            + self.left_operand.to_python()
            + type_hint
            + " "
            + self.OPERATOR_TOKEN_TYPES_TO_PYTHON[self.operator.token_type]
            + " "
            + self.right_operand.to_python()
            + right_bracket
        )
