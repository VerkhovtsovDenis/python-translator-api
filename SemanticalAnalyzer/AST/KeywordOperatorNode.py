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
        indent = " " * indent_level

        if self.operator_token.token_type == TokenTypes.WRITE:
            params += ", sep=''"

        return indent + python_code + "(" + params + ")"

    KEYWORDOPERATOR_TOKEN_TYPES_TO_GO = {
        TokenTypes.WRITELN: "fmt.Println",
        TokenTypes.WRITE: "fmt.Println",
        TokenTypes.READ: "fmt.Scanln",
        TokenTypes.READLN: "fmt.Scanln",
    }
    
    def to_go(self, indent_level, variables) -> str:
        go = self.KEYWORDOPERATOR_TOKEN_TYPES_TO_GO[
            self.operator_token.token_type
        ]
        params = ", ".join(param.to_go(indent_level=0, variables=variables) for param in self.params)
        indent = " " * indent_level

        return indent + go + "(" + params + ")"