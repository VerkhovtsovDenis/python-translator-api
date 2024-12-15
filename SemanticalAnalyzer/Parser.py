from typing import Generator

from .AST import (
    ExpressionNode,
    StatementsNode,
    ValueNode,
    VariableNode,
    BinaryOperatorNode,
    UnarOperatorNode,
    KeywordOperatorNode,
)
from .Variable import (
    Variable,
    TOKEN_TYPE_TO_DATA_TYPE_MAP,
    VALUE_TOKEN_TYPE_TO_DATA_TYPE,
    BaseDataType,
)

from .Erorrs import (
    RedeceredIdError,
    UnExpectedTokenError,
    TypeError,
    UnknowIdError,
)
from LexicalAnalyzer import (
    Token,
    TokenType,
    TokenTypes,
    KEYWORDS_OPERATORS_TOKENS,
    VALUES,
    DATA_TYPES_TOKENS,
    OPERATORS_TOKENS,
)


class Parser:
    """Класс парсера."""

    def __init__(self, tokens_generator: Generator[Token, None, None]):
        self._tokens_generator = tokens_generator
        self._current_token = None
        self._previous_token = None

        self._global_scope: dict[str, Variable] = {}

    def _next_token(self):
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
            bool: Входит ли тип текущего токена в множество переданных.
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
            UnExpectedTokenError: Ожидался другой токен.
        """

        if not self._match(*expected_tokens_type):
            raise UnExpectedTokenError(
                expected_tokens=expected_tokens_type,
                actual_token=self._current_token.token_type,
                line=self._current_token.line,
                pos=self._current_token.pos,
            )

    def _check_varibale_in_scope(self):
        """
        Проверяет, что текущий токен есть в скоупе.

        Raises:
            UnExpectedTokenError: Текущий токен не идентификатор.
            UnknowIdError: Текущего токена нет в скоупе.
        """
        self._require(TokenTypes.ID)
        if self._current_token.value not in self._global_scope:
            raise UnknowIdError(
                self._current_token.value,
                self._current_token.line,
                self._current_token.pos,
            )

    def _parse_var_block(self):
        """Парсит секцию var, когда текущий токен на ключевом слове var"""
        self._require(TokenTypes.VAR)
        self._next_token()

        while self._match(TokenTypes.ID):
            self._parse_type_scope()
            self._next_token()

    def _parse_type_scope(self):
        """Парсит объявление переменных одного из типов данных"""
        # TODO нужно добавлять в аст присвоения с значениями по умолчанию для переменных.
        variables_names: list[str] = []

        self._require(TokenTypes.ID)
        variables_names.append(self._current_token.value)
        self._next_token()

        while not self._match(TokenTypes.COLON):
            self._require(TokenTypes.COMMA)
            self._next_token()
            self._require(TokenTypes.ID)
            variables_names.append(self._current_token.value)
            self._next_token()

        self._next_token()
        self._require(*DATA_TYPES_TOKENS)

        varibales_type = TOKEN_TYPE_TO_DATA_TYPE_MAP[self._current_token.token_type]

        for variable_name in variables_names:
            if variable_name in self._global_scope:
                raise RedeceredIdError(id=variable_name)
            varibale = Variable(varibales_type, variable_name)
            self._global_scope[variable_name] = varibale

        self._next_token()
        self._require(TokenTypes.SEMICOLON)

    def _parse_program_block(self):
        """Парсит блок program."""
        self._require(TokenTypes.PROGRAM)
        self._next_token()

        self._require(TokenTypes.ID)
        self._next_token()

        self._require(TokenTypes.SEMICOLON)
        self._next_token()

    def _parse_code_block(self) -> list[ExpressionNode]:
        """
        Парсит блок кода. Все что между begin и end.

        Returns:
            list[ExpressionNode]: Список узлов ast.
        """
        nodes = []

        self._require(TokenTypes.BEGIN)
        self._next_token()

        while not self._match(TokenTypes.END):
            node = self._parse_code_str()
            nodes.append(node)

        self._require(TokenTypes.END)
        self._next_token()

        return nodes

    def _parse_code_str(self) -> ExpressionNode:
        """
        Парсит одну строчку кода.

        Returns:
            ExpressionNode: Узел ast.
        """
        # Первым в строчке кода может быть оператор, переменная, ...
        if self._match(*KEYWORDS_OPERATORS_TOKENS):
            keyword_operator_node = self._parse_keyword_operator()
            self._require(TokenTypes.SEMICOLON)
            self._next_token()
            return keyword_operator_node
        elif self._match(TokenTypes.ID):
            # Если первой в строчке переменная, это обязательно операция присваивания.
            self._check_varibale_in_scope()

            variable_node = VariableNode(
                self._current_token,
                self._global_scope[self._current_token.value].data_type,
            )
            self._next_token()

            self._require(TokenTypes.ASSIGNMENT)
            operator_token = self._current_token
            self._next_token()

            right_part = self._parse_formula(
                self._global_scope[variable_node.variable.value].data_type
            )

            self._require(TokenTypes.SEMICOLON)
            self._next_token()

            return BinaryOperatorNode(operator_token, variable_node, right_part)

    def _parse_formula(
        self, expected_type: BaseDataType, brackets=False
    ) -> ExpressionNode:
        """
        Парсит формулу. Формула, это все то что может идти после оператора присваивания.

        Args:
        expected_type (BaseDataType): Ожидаемый тип данных для формулы.

        Returns:
            ExpressionNode: Узел ast.

        Raises:
            TypeError: При не соответсвии типов.
        """
        left_node = (
            self._parse_brackets_formula(expected_type)
            if self._match(TokenTypes.LEFT_BRACKET)
            else self._parse_value_or_id(expected_type)
        )
        operator = self._current_token if self._match(*OPERATORS_TOKENS) else None

        while operator:
            self._next_token()
            right_node = (
                self._parse_brackets_formula(expected_type)
                if self._match(TokenTypes.LEFT_BRACKET)
                else self._parse_value_or_id(expected_type)
            )
            left_node = BinaryOperatorNode(
                operator, left_node, right_node, brackets=brackets
            )
            operator = self._current_token if self._match(*OPERATORS_TOKENS) else None
        return left_node

    def _parse_value_or_id(
        self, expected_type: BaseDataType = None, without_type_check=False
    ):
        """
        Парсит значение или идентификатор.

        Args:
        expected_type (BaseDataType): Ожидаемый тип данных.

        Returns:
            ExpressionNode: Узел ast.

        Raises:
            TypeError: При не соответсвии типов.
            UnknowIdError: Текущего токена нет в скоупе.
        """

        self._require(*VALUES, TokenTypes.ID)
        if self._match(*VALUES):

            if (
                not VALUE_TOKEN_TYPE_TO_DATA_TYPE[self._current_token.token_type]
                == expected_type
                and not without_type_check
            ):
                raise TypeError(
                    self._current_token.value,
                    expected_type.__name__,
                    self._current_token.line,
                    self._current_token.pos,
                )
            node = ValueNode(self._current_token, data_type=expected_type)
            self._next_token()
            return node

        else:
            self._check_varibale_in_scope()
            if (
                self._global_scope[self._current_token.value].data_type != expected_type
                and not without_type_check
            ):
                raise TypeError(
                    self._current_token.value,
                    expected_type.__name__,
                    self._current_token.line,
                    self._current_token.pos,
                )
            node = VariableNode(self._current_token, data_type=expected_type)
            self._next_token()
            return node

    def _parse_brackets_formula(self, expected_type: BaseDataType) -> ExpressionNode:
        """
        Парсит формулу в скобках.

        Args:
        expected_type (BaseDataType): Ожидаемый тип данных для формулы.

        Returns:
            ExpressionNode: Узел ast.

        Raises:
            TypeError: При не соответсвии типов.
        """
        self._require(TokenTypes.LEFT_BRACKET)
        self._next_token()
        node = self._parse_formula(expected_type, brackets=True)
        self._require(TokenTypes.RIGHT_BRACKET)
        self._next_token()
        return node

    def _parse_keyword_operator(self):
        """Парсит оператор-ключевое слово."""
        self._require(*KEYWORDS_OPERATORS_TOKENS)
        keyword_token = self._current_token

        self._next_token()
        self._require(TokenTypes.LEFT_BRACKET)
        self._next_token()
        params = []

        while self._match(*VALUES, TokenTypes.ID):
            param_node = self._parse_value_or_id(without_type_check=True)
            params.append(param_node)
            if self._match(TokenTypes.RIGHT_BRACKET):
                break
            self._require(TokenTypes.COMMA)
            self._next_token()

        self._require(TokenTypes.RIGHT_BRACKET)
        self._next_token()

        return KeywordOperatorNode(keyword_token, params)

    def parse_code(self) -> ExpressionNode | None:
        """Парсит весь код."""
        try:
            self._next_token()

            # Парсинг блоков, до основного кода программы.
            while not self._match(TokenTypes.BEGIN):
                if self._current_token.token_type == TokenTypes.PROGRAM:
                    self._parse_program_block()

                if self._current_token.token_type == TokenTypes.VAR:
                    self._parse_var_block()

            # Для упрощения тестирования секция основоного кода не обязательная.
            # В реальных компиляторах секция она обязательна.
            if self._current_token.token_type == TokenTypes.BEGIN:
                try:
                    ast = StatementsNode()
                    for node in self._parse_code_block():
                        ast.add_node(node)
                    self._require(TokenTypes.DOT)

                    return ast
                except StopIteration:
                    raise UnExpectedTokenError("Dot expected.")
                    self._require(TokenTypes.DOT)
        except StopIteration:
            pass
        finally:
            print("Парсинг завершен.")
