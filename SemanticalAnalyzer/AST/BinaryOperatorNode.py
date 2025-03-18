from .ExpressionNode import ExpressionNode
from LexicalAnalyzer import Token, TokenTypes
from SemanticalAnalyzer.Variable import DATA_TYPES_TO_PYTHON, DATA_TYPES_TO_GO


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
        TokenTypes.AND: "and",
        TokenTypes.OR: "or",
        TokenTypes.NOT: "not",
        TokenTypes.EQUAL: "==",
        TokenTypes.NOT_EQUAL: "!=",
        TokenTypes.LESS_THAN: "<",
        TokenTypes.GREATER_THAN: ">",
        TokenTypes.LESS_THAN_OR_EQUAL: "<=",
        TokenTypes.GREATER_THAN_OR_EQUAL: ">=",
    }

    def to_python(self, indent_level) -> str:
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

        indent = " " * indent_level
        return (
            indent
            + left_bracket
            + self.left_operand.to_python(indent_level=0)
            + type_hint
            + " "
            + self.OPERATOR_TOKEN_TYPES_TO_PYTHON[self.operator.token_type]
            + " "
            + self.right_operand.to_python(indent_level=0)
            + right_bracket
        )

    
    OPERATOR_TOKEN_TYPES_TO_GO = {
        TokenTypes.PLUS: "+",
        TokenTypes.MINUS: "-",
        TokenTypes.MULTIPLY: "*",
        TokenTypes.DIVISION: "/",
        TokenTypes.DIV: "//",
        TokenTypes.MOD: "%",
        TokenTypes.ASSIGNMENT: "=",
        TokenTypes.AND: "&&",
        TokenTypes.OR: "||",
        TokenTypes.NOT: "!",
        TokenTypes.EQUAL: "==",
        TokenTypes.NOT_EQUAL: "!=",
        TokenTypes.LESS_THAN: "<",
        TokenTypes.GREATER_THAN: ">",
        TokenTypes.LESS_THAN_OR_EQUAL: "<=",
        TokenTypes.GREATER_THAN_OR_EQUAL: ">=",
    }
    

    
    def to_go(self, indent_level, variables) -> str:
        """
        Преобразует ноду дерева в питон.

        Raises:
            NotImplementedError: Метод не реализован.
        """
        go_variables = variables
        
        left_bracket, right_bracket = "", ""
        if self.brackets:
            left_bracket, right_bracket = "(", ")"

        type_hint = ""
        assigment_prefix = ""
        if self.operator.token_type == TokenTypes.ASSIGNMENT and self.type_hint:
            if self.left_operand.to_go(indent_level=0, variables=variables) not in go_variables:
                go_variables.append(self.left_operand.to_go(indent_level=0, variables=variables))
                assigment_prefix = "var "
            type_hint = f" {DATA_TYPES_TO_GO[self.left_operand.data_type]}"

        indent = " " * indent_level
        return (
            indent
            + left_bracket
            + assigment_prefix
            + self.left_operand.to_go(indent_level=0, variables=variables)
            + type_hint
            + " "
            + self.OPERATOR_TOKEN_TYPES_TO_GO[self.operator.token_type]
            + " "
            + self.right_operand.to_go(indent_level=0, variables=variables)
            + right_bracket
        )