from typing import Any
from LexicalAnalyzer import TokenType, TokenTypes
from .Erorrs import SemanticError


class BaseDataType:
    """Базовый класс для типов данных."""
    token_type: TokenType = None

    def check_value(self, value: Any) -> bool:
        """
        Проверяет принадлежит ли переданное значение типу данных.
        Args:
            value (Any): любое значение.

        Raises:
            NotImplementedError: Метод не реализован.
        """
        raise SemanticError


class IntegerDataType(BaseDataType):
    token_type = TokenTypes.INTEGER_TYPE

    def check_value(self, value):
        try:
            int(value)
            return True
        finally:
            return False


class RealDataType(BaseDataType):
    token_type = TokenTypes.REAL_TYPE

    def check_value(self, value):
        try:
            float(value)
            return True
        finally:
            return False


class StringDataType(BaseDataType):
    token_type = TokenTypes.STRING_TYPE

    def check_value(self, value):
        try:
            str(value)
            return True
        finally:
            return False


class CharDataType(BaseDataType):
    token_type = TokenTypes.CHAR_TYPE

    def check_value(self, value):
        try:
            str(value)
            return len(str(value)) == 1
        finally:
            return False


class BooleanDateType(BaseDataType):
    token_type = TokenTypes.BOOLEAN_TYPE

    def check_value(self, value):
        try:
            bool(value)
            return True
        finally:
            return False


TOKEN_TYPE_TO_DATA_TYPE_MAP = {
    TokenTypes.INTEGER_TYPE: IntegerDataType,
    TokenTypes.REAL_TYPE: RealDataType,
    TokenTypes.STRING_TYPE: StringDataType,
    TokenTypes.CHAR_TYPE: CharDataType,
    TokenTypes.BOOLEAN_TYPE: BooleanDateType,
}


class Variable:
    def __init__(self, data_type: BaseDataType, name: str):
        self.data_type = data_type
        self.name = name
        self.value = None

    def set_value(self, value):
        self.value = value

    def __str__(self):
        return (
            f"(Переменная: {self.data_type.__name__}, {self.name}"
            ", значение:{self.value})"
        )

    def __repr__(self):
        return self.__str__()

    def __eq__(self, value):
        return (
            isinstance(value, Variable)
            and self.name == value.name
            and self.data_type == value.data_type
        )
