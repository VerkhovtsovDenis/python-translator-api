import re
from typing import Generator

from .Errors import (
    InvalidTokensError,
    UnknowTokenError,
)
from .Token import Token
from .TokenType import TokenTypes, OPERATORS_TOKENS, DELIMETERS_TOKENS


class Lexer:
    """
    Класс лексическкого анализатора, отвечающий за генерацию последовательности токенов
    и первичный ее анализ.
    """

    # Типы токенов, которые не будут возвращены
    UNIMPORTANT_TOKENS = (
        TokenTypes.TABULATION,
        TokenTypes.NEWLINE,
        TokenTypes.WHITESPACE,
        TokenTypes.MULTI_LINE_COMMENT,
        TokenTypes.SINGLE_LINE_COMMENT,
    )

    def __init__(self, *, code: str):
        """
        Args:
            code (str): Код входной программы на паскале.
        """
        self._input = code
        self._input_len = len(code)

        self._line = 0
        self._pos = 0  # Абсолютная позиция указателя
        self._relative_pos = (
            0  # Позиция указателя, относительно текущей анализируемой строки
        )

    def _increment_pos(self, inc: int = 1):
        """
        Инкрементирует абсолютную и относительную позицию указателя.

        Args:
            inc (int): Число, на которое нужно инкрементировать указатель.
        """
        self._pos += inc
        self._relative_pos += inc

    def tokenize(self) -> Generator[Token, None, None]:
        """
        Создает генератор, запускающий процес лексического анализа.

        Returns:
            Generator[Token, None, None]: Генератор, возвращающий токены.

        Raises:
            SyntaxError: Синтаксическая ошибка.
        """
        token = self._get_next_token()
        while token:
            self._postprocess(token)

            if token.token_type not in self.UNIMPORTANT_TOKENS:
                yield token

            token = self._get_next_token()

    def _get_next_token(self) -> Token | None:
        """
        Возвращает следующий токен и передвигает указатели.

        Returns:
            Token | None: Следующий токен.
        """
        if self._pos >= self._input_len:
            return None

        self._preprocess()

        # Часть инпута, анализируемая сейчас
        text = self._input[self._pos : len(self._input)]

        possible_tokens: list[Token] = []

        # Находит возможные токены
        for token_type in TokenTypes:
            regex = token_type.value.regex
            result = re.match(regex, text, flags=re.I)

            if result:
                string = result.group(0)
                value = result.group(1)
                token = Token(
                    token_type=token_type,
                    string=string,
                    value=value,
                    line=self._line,
                    pos=self._relative_pos,
                )
                possible_tokens.append(token)

        if not possible_tokens:
            raise UnknowTokenError(
                code=self._input[self._pos],
                line=self._line,
                pos=self._relative_pos,
            )

        # За правильный токен, считаем самый длинный из возможных

        # Например последовательность 'begin_value'
        # Может быть токеном ключевого словом 'begin'
        # Или токеном идентификатора 'begin_value'
        # И правильным будет самый длинный токен

        token = max(possible_tokens, key=lambda x: len(x.string))

        return token

    def _preprocess(self):
        """перемещает указатель self._pos на последний не пробельный символ."""

        if self._input[self._pos] not in (" ", "\t"):
            return

        next_pos = self._pos + 1

        while next_pos < self._input_len and self._input[next_pos] in (" ", "\t"):
            next_pos += 1

        inc = next_pos - self._pos - 1
        self._increment_pos(inc)

    def _postprocess(self, token: Token):
        """
        Логика после нахождения токена. Передвигает указатель.
        Находит ошибки, связанные с недопустимым расположением токенов.

        Args:
            token (Token): Токен найденный на текущем шаге анализатора.
        """
        # Опасные токены для которых нужно сделать проверку следующего токена
        # Опытным путем было выявленно, что следующим токеном для них обязан быть
        # Разделитель, либо оператор
        DANGEROUS_TOKEN_TYPES = (
            TokenTypes.NUMBER_INTEGER,
            TokenTypes.NUMBER_REAL,
            TokenTypes.STRING,
            TokenTypes.STRING,
        )

        self._increment_pos(len(token.string))

        if token.token_type in (TokenTypes.MULTI_LINE_COMMENT, TokenTypes.NEWLINE):
            self._line += token.string.count("\n")
            self._relative_pos = 0

        # ищем ошибки для опасных токенов
        if token.token_type in DANGEROUS_TOKEN_TYPES:
            next_token = self._get_next_token()
            if next_token.token_type not in OPERATORS_TOKENS + DELIMETERS_TOKENS:
                raise InvalidTokensError(
                    code=self._input[
                        self._pos - len(token.value) : self._pos + len(next_token.value)
                    ],
                    line=token.line,
                    pos=token.pos,
                )
