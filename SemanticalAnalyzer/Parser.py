from .AST import (
    ExpressionNode,
    StatementsNode,
    NumberNode,
    VariableNode,
    BinaryOperatorNode,
    UnarOperatorNode,
)
from LexicalAnalyzer import Token, TokenType, TokenTypes


class Parser:
    """Класс парсера"""

    KEY_WORDS_TOKENS = (
        TokenTypes.BEGIN,
        TokenTypes.END,
        TokenTypes.PROGRAM,
        TokenTypes.CONST,
        TokenTypes.VAR,
        TokenTypes.FUNCTION,
        TokenTypes.PROCEDURE,
        TokenTypes.ARRAY,
    )

    NUMBERS_TOKENS = (
        TokenTypes.NUMBER_INTEGER,
        TokenTypes.NUMBER_REAL,
        TokenTypes.STRING,
    )

    OPERATORS = (
        TokenTypes.EQUAL,
        TokenTypes.NOT_EQUAL,
        TokenTypes.LESS_THAN,
        TokenTypes.GREATER_THAN,
        TokenTypes.LESS_THAN_OR_EQUAL,
        TokenTypes.GREATER_THAN_OR_EQUAL,
        TokenTypes.PLUS,
        TokenTypes.MINUS,
        TokenTypes.MULTIPLY,
        TokenTypes.DIVISION,
        TokenTypes.MOD,
        TokenTypes.DIV,
        # other logical and, or, not
    )

    def __init__(self, tokens: list[Token]):
        self.tokens: list[Token] = tokens
        self.pos = 0

        self.scope = {}

    def match(self, *expected_tokens_type: list[TokenType]) -> Token | None:
        """
        Получение токена по его номеру в последовательности токенов. если токен входит в множество допустимых токенов.

        Args:
            expected_tokens_type (list[TokenType]): множество допустимых токенов.

        Returns:
            Token|None: Найденный токен.
        """
        if self.pos < len(self.tokens):
            curent_token = self.tokens[self.pos]

            if curent_token.token_type in expected_tokens_type:
                self.pos += 1
                return curent_token

    def require(self, expected_tokens_type: list[TokenType]) -> Token:
        """
        Требует что бы по self.pos был токен из переданного множества токенов иниче вызывает исключение
        Args:
            expected_tokens_type (list[TokenType]): множество допустимых токенов.

        Returns:
            Token|None: Найденный токен.
            // TO DO ПОСМОТРЕТЬ НА РАБОТЕ КАК ОБОЗНАЧАТЬ ЧТО МОЖЕТ БЫТЬ RAISE
        """
        token = self.match(expected_tokens_type=expected_tokens_type)
        if not token:
            raise ValueError(
                f"на позщиции {self.pos} ожидается токен из {expected_tokens_type}"
            )

        return token

    def parse_variable_or_number(self):
        number_token = self.match(expected_tokens_type=self.NUMBERS_TOKENS)
        if number_token:
            return NumberNode(number_token)

        varible_token = self.match(TokenTypes.ID)

        if varible_token:
            return VariableNode(varible_token)

        raise ValueError("Ожидалось число или идентификатор")

    def parse_parentheses(self) -> ExpressionNode:
        """Парсит выражение в скобках"""
        if self.match(TokenTypes.LEFT_BRACKET):
            node = self.parse_formula()
            self.require(TokenTypes.RIGHT_BRACKET)
            return node
        else:
            return self.parse_variable_or_number()

    def parse_formula(self) -> ExpressionNode:
        """парсит математическое выражение"""
        left_node = self.parse_parentheses()
        operator_token = self.math(expected_tokens_type=self.OPERATORS)

        while operator_token:
            right_token = self.parse_parentheses()
            left_node = BinaryOperatorNode(operator_token, left_node, right_token)
            operator_token = self.math(expected_tokens_type=self.OPERATORS)

        return left_node

    def parse_expression(self):
        """Парсит одно вырпжение"""
        if self.match(expected_tokens_type=self.KEY_WORDS_TOKENS):
            key_word_node = self.parse_key_word()
            return key_word_node

        elif self.match(expected_tokens_type=TokenTypes.ID):
            self.pos -= 1
            id_node = self.parse_id()
            assign_operator_token = self.match(TokenTypes.ASSIGNMENT)
            if assign_operator_token:
                right_operand_token = self.parse_formula()
                left_operand_token = id_node
                binary_operator_node = BinaryOperatorNode(
                    assign_operator_token, left_operand_token, right_operand_token
                )
                return binary_operator_node
        raise ValueError("lexic error")

    def parse_writeln(self) -> ExpressionNode:
        writeln_token = self.match(expected_tokens_type=TokenTypes.WRITELN)
        if writeln_token:
            operand = self.parse_parentheses()
            return UnarOperatorNode(writeln_token, operand)
        else:
            raise ValueError()

    def parse_code(self) -> ExpressionNode:
        """парсит весь код"""
        root = StatementsNode()

        while self.pos < len(self.tokens):
            code_string_node = self.parse_expression()
            self.require(expected_tokens_type=TokenTypes.SEMICOLON)
            root.add_node(code_string_node)
        return root
