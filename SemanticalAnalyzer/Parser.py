from typing import Generator
from .AST import (
    ExpressionNode,
    StatementsNode,
    NumberNode,
    VariableNode,
    BinaryOperatorNode,
    UnarOperatorNode,
)
from .Variable import Variable, TOKEN_TYPE_TO_DATA_TYPE_MAP
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

    OPERATORS_TOKENS = (
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

    DATA_TYPES_TOKENS = (
        TokenTypes.INTEGER_TYPE,
        TokenTypes.CHAR_TYPE,
        TokenTypes.STRING_TYPE,
        TokenTypes.BOOLEAN_TYPE,
        TokenTypes.REAL_TYPE,
    )

    def __init__(self, tokens_generator: Generator[Token, None, None]):
        self._tokens_generator = tokens_generator
        self._current_token = None
        self._previous_token = None

        self._global_scope: dict[str, Variable] = {}

    def _get_next_token(self):
        """
        Передвигает self._current_token на следующий токен из генератора self._tokens_generator.

        Args:
            expected_tokens_type (list[TokenType]): множество допустимых токенов.

        Raises:
            StopIteration: Если токены в генераторе закончились.
        """
        self._previous_token = self._current_token
        self._current_token = next(self._tokens_generator)

    def _match(self, *expected_tokens_type: tuple[TokenType]) -> bool:
        """
        Проверяет, что тип текущего токена входит в множество переднных типов.

        Args:
            expected_tokens_type (list[TokenType]): множество допустимых типов токенов.

        Returns:
            bool: входит ли тип текущего токена в множество переданных.
        """
        if self._current_token.token_type in expected_tokens_type:
            return True

    def _require(self, *expected_tokens_type: tuple[TokenType]):
        """
        Требует чтобы  был тип текущего токена входил в множество переаднных типов,
        иначе вызывает исключение
        Args:
            expected_tokens_type (list[TokenType]): множество допустимых типов токенов.

        Raises:
            ValueError: Dash app required for force init callbacks.
        """

        if not self._match(*expected_tokens_type):
            raise ValueError(
                f"""на позщиции {self._current_token.pos} ожидается токен из {expected_tokens_type}\n
                а был получен {self._current_token}"""
            )

    def parse_variable_or_number(self):
        number_token = self._match(*self.NUMBERS_TOKENS)
        if number_token:
            return NumberNode(number_token)

        varible_token = self._match(TokenTypes.ID)

        if varible_token:
            return VariableNode(varible_token)

        raise ValueError("Ожидалось число или идентификатор")

    def parse_parentheses(self) -> ExpressionNode:
        """Парсит выражение в скобках"""
        if self._match(TokenTypes.LEFT_BRACKET):
            node = self.parse_formula()
            self._require(TokenTypes.RIGHT_BRACKET)
            return node
        else:
            return self.parse_variable_or_number()

    def parse_formula(self) -> ExpressionNode:
        """Парсит математическое выражение"""
        left_node = self.parse_parentheses()
        operator_token = self.math(expected_tokens_type=self.OPERATORS)

        while operator_token:
            right_token = self.parse_parentheses()
            left_node = BinaryOperatorNode(operator_token, left_node, right_token)
            operator_token = self.math(expected_tokens_type=self.OPERATORS)

        return left_node

    def parse_expression(self):
        """Парсит одно выражение"""
        if self._match(*self.KEY_WORDS_TOKENS):
            key_word_node = self.parse_key_word()
            return key_word_node

        elif self._match(TokenTypes.ID):
            self.pos -= 1
            id_node = self.parse_id()
            assign_operator_token = self._match(TokenTypes.ASSIGNMENT)
            if assign_operator_token:
                right_operand_token = self.parse_formula()
                left_operand_token = id_node
                binary_operator_node = BinaryOperatorNode(
                    assign_operator_token, left_operand_token, right_operand_token
                )
                return binary_operator_node
        raise ValueError("lexic error")

    def parse_writeln(self) -> ExpressionNode:
        writeln_token = self._match(TokenTypes.WRITELN)
        if writeln_token:
            operand = self.parse_parentheses()
            return UnarOperatorNode(writeln_token, operand)
        else:
            raise ValueError()

    def _parse_global_scope(self):
        """Парсит секцию var, когда текущий токен на ключевом слове var"""
        self._require(TokenTypes.VAR)
        self._get_next_token()

        while self._match(TokenTypes.ID):
            self._parse_type_scope()
            self._get_next_token()

    def _parse_type_scope(self):
        """Парсит объявление переменных одного из типов данных"""
        variables_names: list[str] = []

        self._require(TokenTypes.ID)
        variables_names.append(self._current_token.value)
        self._get_next_token()

        while not self._match(TokenTypes.COLON):
            self._require(TokenTypes.COMMA)
            self._get_next_token()
            self._require(TokenTypes.ID)
            variables_names.append(self._current_token.value)
            self._get_next_token()

        self._get_next_token()
        self._require(*self.DATA_TYPES_TOKENS)

        varibales_type = TOKEN_TYPE_TO_DATA_TYPE_MAP[self._current_token.token_type]

        for variable_name in variables_names:

            varibale = Variable(varibales_type, variable_name)
            self._global_scope[variable_name] = varibale

        self._get_next_token()
        self._require(TokenTypes.SEMICOLON)

    def parse_code(self) -> ExpressionNode:
        """парсит весь код"""
        root = StatementsNode()
        self._get_next_token()

        if self._current_token.token_type == TokenTypes.VAR:
            self._parse_global_scope()

        print(self._global_scope)

        # while self.pos < len(self.tokens):
        #     code_string_node = self.parse_expression()
        #     self._require(expected_tokens_type=TokenTypes.SEMICOLON)
        #     root.add_node(code_string_node)
        # return root
