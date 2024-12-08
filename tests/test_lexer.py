# flake8: noqa: F401
import os
import sys
import pytest

from LexicalAnalyzer import Lexer, FileManager, TokenTypes
from LexicalAnalyzer import (
    InvalidNumberFormatError,
    UnexpectedTokenSequenceError,
    InvalidRealNumberFormatError,
    UnmatchedParenthesisError,
    UnclosedStringLiteralError,
)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def test_can_lexer_init():
    path = r"\tests\lexer_code\1.pas"
    pascal_code = FileManager.get_code(path)
    tokens = Lexer(code=pascal_code).tokenize()


def test_get_lexem_1pas():
    path = r"\tests\lexer_code\1.pas"
    pascal_code = FileManager.get_code(path)
    tokens = list(Lexer(code=pascal_code).tokenize())
    delimeters_tokens = tokens

    correct_tokens_subsequence = [
        TokenTypes.WHITESPACE,
        TokenTypes.BEGIN,
        TokenTypes.NEWLINE,
        TokenTypes.WHITESPACE,
        TokenTypes.WRITELN,
        TokenTypes.LEFT_BRACKET,
        TokenTypes.STRING,
        TokenTypes.RIGHT_BRACKET,
        TokenTypes.SEMICOLON,
        TokenTypes.WHITESPACE,
        TokenTypes.SINGLE_LINE_COMMENT,
        TokenTypes.WHITESPACE,
        TokenTypes.END,
        TokenTypes.DOT,
    ]

    for token, corrett_token_type in zip(delimeters_tokens, correct_tokens_subsequence):
        assert token.token_type == corrett_token_type


def test_get_lexem_2pas():
    path = r"\tests\lexer_code\2.pas"
    pascal_code = FileManager.get_code(path)
    tokens = list(Lexer(code=pascal_code).tokenize())
    delimeters_tokens = tokens

    correct_tokens_subsequence = [
        TokenTypes.VAR,
        TokenTypes.NEWLINE,
        TokenTypes.WHITESPACE,
        TokenTypes.ID,
        TokenTypes.COMMA,
        TokenTypes.ID,
        TokenTypes.COLON,
        TokenTypes.WHITESPACE,
        TokenTypes.REAL_TYPE,
        TokenTypes.SEMICOLON,
        TokenTypes.NEWLINE,
        TokenTypes.WHITESPACE,
        TokenTypes.ID,
        TokenTypes.COLON,
        TokenTypes.WHITESPACE,
        TokenTypes.REAL_TYPE,
        TokenTypes.SEMICOLON,
        TokenTypes.NEWLINE,
        TokenTypes.WHITESPACE,
        TokenTypes.BEGIN,
        TokenTypes.NEWLINE,
        TokenTypes.WHITESPACE,
        # многострочный комментарий не пребовляет в токен строки
        TokenTypes.MULTI_LINE_COMMENT,
        TokenTypes.NEWLINE,
        # строка 9
        TokenTypes.WHITESPACE,
        TokenTypes.WRITE,
        TokenTypes.LEFT_BRACKET,
        TokenTypes.STRING,
        TokenTypes.RIGHT_BRACKET,
        TokenTypes.SEMICOLON,
        TokenTypes.NEWLINE,
        TokenTypes.WHITESPACE,
        TokenTypes.READLN,
        TokenTypes.LEFT_BRACKET,
        TokenTypes.ID,
        TokenTypes.RIGHT_BRACKET,
        TokenTypes.SEMICOLON,
        TokenTypes.NEWLINE,
        TokenTypes.WHITESPACE,
        TokenTypes.ID,
        TokenTypes.WHITESPACE,
        TokenTypes.ASSIGNMENT,
        TokenTypes.WHITESPACE,
        TokenTypes.NUMBER_REAL,
        TokenTypes.NEWLINE,
        # строка 12
        TokenTypes.WHITESPACE,
        TokenTypes.WRITE,
        TokenTypes.LEFT_BRACKET,
        TokenTypes.STRING,
        TokenTypes.RIGHT_BRACKET,
        TokenTypes.SEMICOLON,
        TokenTypes.NEWLINE,
        TokenTypes.WHITESPACE,
        TokenTypes.READLN,
        TokenTypes.LEFT_BRACKET,
        TokenTypes.ID,
        TokenTypes.RIGHT_BRACKET,
        TokenTypes.SEMICOLON,
        TokenTypes.NEWLINE,
        TokenTypes.WHITESPACE,
        TokenTypes.ID,
        TokenTypes.WHITESPACE,
        TokenTypes.ASSIGNMENT,
        TokenTypes.WHITESPACE,
        TokenTypes.ID,
        TokenTypes.LEFT_BRACKET,
        TokenTypes.ID,
        TokenTypes.MINUS,
        TokenTypes.ID,
        TokenTypes.RIGHT_BRACKET,
        TokenTypes.SEMICOLON,
        TokenTypes.NEWLINE,
        # строка 15
        TokenTypes.WHITESPACE,
        TokenTypes.WRITELN,
        TokenTypes.LEFT_BRACKET,
        TokenTypes.STRING,
        TokenTypes.COMMA,
        TokenTypes.WHITESPACE,
        TokenTypes.ID,
        TokenTypes.RIGHT_BRACKET,
        TokenTypes.SEMICOLON,
        TokenTypes.NEWLINE,
        # строка 16
        TokenTypes.WHITESPACE,
        TokenTypes.END,
        TokenTypes.DOT,
    ]

    for token, corrett_token_type in zip(delimeters_tokens, correct_tokens_subsequence):
        if token.token_type != TokenTypes.MULTI_LINE_COMMENT:
            assert token.token_type == corrett_token_type
        else:
            # Проверить код
            assert token.token_type == corrett_token_type


@pytest.mark.xfail
def test_get_lexem_3pas():
    path = r"\tests\lexer_code\3.pas"
    pascal_code = FileManager.get_code(path)

    with pytest.raises(InvalidNumberFormatError):
        list(Lexer(code=pascal_code).tokenize())


@pytest.mark.xfail
def test_get_lexem_4pas():
    path = r"\tests\lexer_code\4.pas"
    pascal_code = FileManager.get_code(path)

    with pytest.raises(UnexpectedTokenSequenceError):
        list(Lexer(code=pascal_code).tokenize())


@pytest.mark.xfail
def test_get_lexem_5pas():
    path = r"\tests\lexer_code\5.pas"
    pascal_code = FileManager.get_code(path)

    with pytest.raises(InvalidRealNumberFormatError):
        list(Lexer(code=pascal_code).tokenize())


@pytest.mark.xfail
def test_get_lexem_6pas():
    path = r"\tests\lexer_code\6.pas"
    pascal_code = FileManager.get_code(path)

    with pytest.raises(UnmatchedParenthesisError):
        list(Lexer(code=pascal_code).tokenize())


@pytest.mark.xfail
def test_get_lexem_7pas():
    path = r"\tests\lexer_code\7.pas"
    pascal_code = FileManager.get_code(path)

    with pytest.raises(UnclosedStringLiteralError):
        list(Lexer(code=pascal_code).tokenize())


if __name__ == "__main__":
    test_get_lexem_2pas()
