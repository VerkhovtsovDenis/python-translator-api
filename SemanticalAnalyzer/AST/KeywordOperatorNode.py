from LexicalAnalyzer import TokenTypes
from .ExpressionNode import ExpressionNode
from LexicalAnalyzer import Token


class KeywordOperatorNode(ExpressionNode):
    """Класс узла операторов для  AST."""

    def __init__(self, operator_token: Token, params: list[ExpressionNode]):
        self.params = params
        self.operator_token = operator_token

    def __eq__(self, value):
        return (
            isinstance(value, KeywordOperatorNode)
            and self.operator_token == value.operator_token
            and self.params == value.params
        )

    KEYWORDOPERATOR_TOKEN_TYPES_TO_PYTHON = {
        TokenTypes.WRITELN: "print",
        TokenTypes.WRITE: "print",
        TokenTypes.READ: "input",
        TokenTypes.READLN: "input",
    }

    def to_python(self, indent_level) -> str:
        python_code = self.KEYWORDOPERATOR_TOKEN_TYPES_TO_PYTHON[
            self.operator_token.token_type
        ]
        params = ", ".join(param.to_python(indent_level=0) for param in self.params)

        if self.operator_token.token_type == TokenTypes.WRITE:
            params += ", sep=''"

        return indent_level * " " + python_code + "(" + params + ")"
