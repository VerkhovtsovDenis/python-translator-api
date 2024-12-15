import pytest

from tests.utils import emulate_tokens_generator
from LexicalAnalyzer import Token, TokenTypes
from SemanticalAnalyzer import (
    Parser,
    RedeceredIdError,
    Variable,
    IntegerDataType,
    RealDataType,
    StringDataType,
    CharDataType,
    BooleanDateType,
    BaseDataType,
)


def test_empty_scope():
    tokens = (
        Token(token_type=TokenTypes.BEGIN),
        Token(token_type=TokenTypes.END),
        Token(token_type=TokenTypes.DOT),
    )
    tokens_genarator = emulate_tokens_generator(tokens)
    parser = Parser(tokens_genarator)
    parser.parse_code()
    assert parser._global_scope == {}


def test_one_varibale_scope():
    tokens = (
        Token(token_type=TokenTypes.VAR),
        Token(token_type=TokenTypes.ID, value="a"),
        Token(token_type=TokenTypes.COLON),
        Token(token_type=TokenTypes.INTEGER_TYPE),
        Token(token_type=TokenTypes.SEMICOLON),
    )
    tokens_genarator = emulate_tokens_generator(tokens)
    parser = Parser(tokens_genarator)
    parser.parse_code()
    assert parser._global_scope == {"a": Variable(IntegerDataType, "a")}


def test_two_varibale_scope():
    tokens = (
        Token(token_type=TokenTypes.VAR),
        Token(token_type=TokenTypes.ID, value="a"),
        Token(token_type=TokenTypes.COMMA),
        Token(token_type=TokenTypes.ID, value="b"),
        Token(token_type=TokenTypes.COLON),
        Token(token_type=TokenTypes.INTEGER_TYPE),
        Token(token_type=TokenTypes.SEMICOLON),
    )
    tokens_genarator = emulate_tokens_generator(tokens)
    parser = Parser(tokens_genarator)
    parser.parse_code()
    assert parser._global_scope == {
        "a": Variable(IntegerDataType, "a"),
        "b": Variable(IntegerDataType, "b"),
    }


def test_two_data_types_scope():
    tokens = (
        Token(token_type=TokenTypes.VAR),
        Token(token_type=TokenTypes.ID, value="a"),
        Token(token_type=TokenTypes.COMMA),
        Token(token_type=TokenTypes.ID, value="b"),
        Token(token_type=TokenTypes.COLON),
        Token(token_type=TokenTypes.INTEGER_TYPE),
        Token(token_type=TokenTypes.SEMICOLON),
        Token(token_type=TokenTypes.ID, value="c"),
        Token(token_type=TokenTypes.COMMA),
        Token(token_type=TokenTypes.ID, value="d"),
        Token(token_type=TokenTypes.COLON),
        Token(token_type=TokenTypes.REAL_TYPE),
        Token(token_type=TokenTypes.SEMICOLON),
    )
    tokens_genarator = emulate_tokens_generator(tokens)
    parser = Parser(tokens_genarator)
    parser.parse_code()
    assert parser._global_scope == {
        "a": Variable(IntegerDataType, "a"),
        "b": Variable(IntegerDataType, "b"),
        "c": Variable(RealDataType, "c"),
        "d": Variable(RealDataType, "d"),
    }


@pytest.mark.parametrize(
    ("data_type"),
    (
        (IntegerDataType),
        (RealDataType),
        (StringDataType),
        (CharDataType),
        (BooleanDateType),
    ),
)
def test_all_data_types_scope(data_type: BaseDataType):
    tokens = (
        Token(token_type=TokenTypes.VAR),
        Token(token_type=TokenTypes.ID, value="a"),
        Token(token_type=TokenTypes.COLON),
        Token(token_type=data_type.token_type),
        Token(token_type=TokenTypes.SEMICOLON),
    )
    tokens_genarator = emulate_tokens_generator(tokens)
    parser = Parser(tokens_genarator)
    parser.parse_code()
    assert parser._global_scope == {
        "a": Variable(data_type, "a"),
    }


def test_redeclared_id_raise():
    tokens = (
        Token(token_type=TokenTypes.VAR),
        Token(token_type=TokenTypes.ID, value="a"),
        Token(token_type=TokenTypes.COLON),
        Token(token_type=TokenTypes.INTEGER_TYPE),
        Token(token_type=TokenTypes.SEMICOLON),
        Token(token_type=TokenTypes.ID, value="a"),
        Token(token_type=TokenTypes.COLON),
        Token(token_type=TokenTypes.INTEGER_TYPE),
        Token(token_type=TokenTypes.SEMICOLON),
    )
    with pytest.raises(RedeceredIdError):
        tokens_genarator = emulate_tokens_generator(tokens)
        parser = Parser(tokens_genarator)
        parser.parse_code()
