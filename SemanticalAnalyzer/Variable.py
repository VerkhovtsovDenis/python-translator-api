from typing import Any
from LexicalAnalyzer import TokenType, TokenTypes
from .Errors import RedeceredIdError


class BaseDataType:
    """Базовый класс для типов данных."""
    token_type: TokenType = None


class IntegerDataType(BaseDataType):
    token_type = TokenTypes.INTEGER_TYPE


class RealDataType(BaseDataType):
    token_type = TokenTypes.REAL_TYPE


class StringDataType(BaseDataType):
    token_type = TokenTypes.STRING_TYPE


class CharDataType(BaseDataType):
    token_type = TokenTypes.CHAR_TYPE


class BooleanDateType(BaseDataType):
    token_type = TokenTypes.BOOLEAN_TYPE


TOKEN_TYPE_TO_DATA_TYPE_MAP = {
    TokenTypes.INTEGER_TYPE: IntegerDataType,
    TokenTypes.REAL_TYPE: RealDataType,
    TokenTypes.STRING_TYPE: StringDataType,
    TokenTypes.CHAR_TYPE: CharDataType,
    TokenTypes.BOOLEAN_TYPE: BooleanDateType,
}

VALUE_TOKEN_TYPE_TO_DATA_TYPE = {
    TokenTypes.NUMBER_INTEGER: IntegerDataType,
    TokenTypes.NUMBER_REAL: RealDataType,
    TokenTypes.STRING: StringDataType,
    TokenTypes.TRUE: BooleanDateType,
    TokenTypes.FALSE: BooleanDateType,
}

DATA_TYPE_TO_BASE_VALUES_MAP = {
    IntegerDataType: "0",
    RealDataType: "0.0",
    StringDataType: "",
    CharDataType: "",
    BooleanDateType: "False",
}

DATA_TYPES_TO_PYTHON = {
    IntegerDataType: "int",
    RealDataType: "float",
    StringDataType: "str",
    CharDataType: "str",
    BooleanDateType: "bool",
}


class Variable:

    def __init__(self, data_type: BaseDataType, name: str):
        self.data_type = data_type
        self.name = name
        self.value = DATA_TYPE_TO_BASE_VALUES_MAP[data_type]

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
