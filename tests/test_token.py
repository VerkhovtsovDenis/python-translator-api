# flake8: noqa: F401
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from LexicalAnalyzer import Lexer, TokenTypes
from FileManager import FileManager


def not_main():
    path = r"\tests\lexer_code\0.pas"
    tokens_lines = FileManager.get_code(path)

    global tokens
    tokens = list(Lexer(code=tokens_lines).tokenize())


def test_delimeters():
    delimeters_tokens = tokens[0:8]
    assert delimeters_tokens[0].token_type == TokenTypes.SEMICOLON
    assert delimeters_tokens[1].token_type == TokenTypes.COLON
    assert delimeters_tokens[2].token_type == TokenTypes.DOT
    assert delimeters_tokens[3].token_type == TokenTypes.COMMA
    assert delimeters_tokens[4].token_type == TokenTypes.LEFT_BRACKET
    assert delimeters_tokens[5].token_type == TokenTypes.RIGHT_BRACKET
    assert delimeters_tokens[5].token_type == TokenTypes.RIGHT_BRACKET

    # FIXME: пробел не считывается как токен
    # assert delimeters_tokens[6].token_type == TokenTypes.WHITESPACE
    assert delimeters_tokens[6].token_type == TokenTypes.TABULATION
    assert delimeters_tokens[7].token_type == TokenTypes.NEWLINE


def test_keywords():
    delimeters_tokens = tokens[8:46:2]
    assert delimeters_tokens[0].token_type == TokenTypes.BEGIN
    assert delimeters_tokens[1].token_type == TokenTypes.END
    assert delimeters_tokens[2].token_type == TokenTypes.PROGRAM
    assert delimeters_tokens[3].token_type == TokenTypes.CONST
    assert delimeters_tokens[4].token_type == TokenTypes.VAR
    assert delimeters_tokens[5].token_type == TokenTypes.FUNCTION
    assert delimeters_tokens[6].token_type == TokenTypes.PROCEDURE
    assert delimeters_tokens[7].token_type == TokenTypes.ARRAY
    assert delimeters_tokens[8].token_type == TokenTypes.WRITELN
    assert delimeters_tokens[9].token_type == TokenTypes.READLN
    assert delimeters_tokens[10].token_type == TokenTypes.IF
    assert delimeters_tokens[11].token_type == TokenTypes.THEN
    assert delimeters_tokens[12].token_type == TokenTypes.ELSE
    assert delimeters_tokens[13].token_type == TokenTypes.FOR
    assert delimeters_tokens[14].token_type == TokenTypes.WHILE
    assert delimeters_tokens[15].token_type == TokenTypes.TO
    assert delimeters_tokens[16].token_type == TokenTypes.DO
    assert delimeters_tokens[17].token_type == TokenTypes.TRUE
    assert delimeters_tokens[18].token_type == TokenTypes.FALSE


def test_types():
    delimeters_tokens = tokens[46:56:2]
    assert delimeters_tokens[0].token_type == TokenTypes.INTEGER_TYPE
    assert delimeters_tokens[1].token_type == TokenTypes.REAL_TYPE
    assert delimeters_tokens[2].token_type == TokenTypes.STRING_TYPE
    assert delimeters_tokens[3].token_type == TokenTypes.CHAR_TYPE
    assert delimeters_tokens[4].token_type == TokenTypes.BOOLEAN_TYPE


def test_operators():
    delimeters_tokens = tokens[56:88:2]
    assert delimeters_tokens[0].token_type == TokenTypes.PLUS
    assert delimeters_tokens[1].token_type == TokenTypes.MINUS
    assert delimeters_tokens[2].token_type == TokenTypes.MULTIPLY
    assert delimeters_tokens[3].token_type == TokenTypes.DIVISION
    assert delimeters_tokens[4].token_type == TokenTypes.DIV
    assert delimeters_tokens[5].token_type == TokenTypes.MOD
    assert delimeters_tokens[6].token_type == TokenTypes.ASSIGNMENT
    assert delimeters_tokens[7].token_type == TokenTypes.EQUAL
    assert delimeters_tokens[8].token_type == TokenTypes.NOT_EQUAL
    assert delimeters_tokens[9].token_type == TokenTypes.LESS_THAN
    assert delimeters_tokens[10].token_type == TokenTypes.GREATER_THAN
    assert delimeters_tokens[11].token_type == TokenTypes.LESS_THAN_OR_EQUAL
    assert delimeters_tokens[12].token_type == TokenTypes.GREATER_THAN_OR_EQUAL
    assert delimeters_tokens[13].token_type == TokenTypes.AND
    assert delimeters_tokens[14].token_type == TokenTypes.OR
    assert delimeters_tokens[15].token_type == TokenTypes.NOT


def test_ids():
    delimeters_tokens = tokens[88:100:2]
    assert delimeters_tokens[0].token_type == TokenTypes.NUMBER_INTEGER
    assert delimeters_tokens[1].token_type == TokenTypes.NUMBER_REAL
    assert delimeters_tokens[2].token_type == TokenTypes.STRING
    assert delimeters_tokens[3].token_type == TokenTypes.ID
    assert delimeters_tokens[4].token_type == TokenTypes.MULTI_LINE_COMMENT
    assert delimeters_tokens[5].token_type == TokenTypes.SINGLE_LINE_COMMENT


if __name__ == "__main__":
    tokens = list(Lexer(code="192.12 ").tokenize())
    print(tokens)
    assert tokens[0].token_type == TokenTypes.NUMBER_REAL

else:
    not_main()
