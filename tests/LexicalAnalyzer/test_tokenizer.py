# flake8: noqa: F401
from LexicalAnalyzer import Lexer, TokenTypes


def assert_tokens_sequence(actual_sequence, expected_sequence):
    for token, corrett_token_type in zip(actual_sequence, expected_sequence):
        assert token.token_type == corrett_token_type


def test_tokens():
    pascal_code = """
    ;:.,()
    begin end program Const var FUNCTION PROCEDURE ARRAY Writeln Readln IF then Else for While To Do True False
    integer real string char Boolean
    + - * / div mod := = <> < > <= >= and or not
    134981 999999.42    'Иван и Людмила' my_token {} // пых пых пых \r
    """
    tokens = Lexer(code=pascal_code).tokenize()
    delimeters_tokens = (
        TokenTypes.SEMICOLON,
        TokenTypes.COLON,
        TokenTypes.DOT,
        TokenTypes.COMMA,
        TokenTypes.LEFT_BRACKET,
        TokenTypes.RIGHT_BRACKET,
        TokenTypes.BEGIN,
        TokenTypes.END,
        TokenTypes.PROGRAM,
        TokenTypes.CONST,
        TokenTypes.VAR,
        TokenTypes.FUNCTION,
        TokenTypes.PROCEDURE,
        TokenTypes.ARRAY,
        TokenTypes.WRITELN,
        TokenTypes.READLN,
        TokenTypes.IF,
        TokenTypes.THEN,
        TokenTypes.ELSE,
        TokenTypes.FOR,
        TokenTypes.WHILE,
        TokenTypes.TO,
        TokenTypes.DO,
        TokenTypes.TRUE,
        TokenTypes.FALSE,
        TokenTypes.INTEGER_TYPE,
        TokenTypes.REAL_TYPE,
        TokenTypes.STRING_TYPE,
        TokenTypes.CHAR_TYPE,
        TokenTypes.BOOLEAN_TYPE,
        TokenTypes.PLUS,
        TokenTypes.MINUS,
        TokenTypes.MULTIPLY,
        TokenTypes.DIVISION,
        TokenTypes.DIV,
        TokenTypes.MOD,
        TokenTypes.ASSIGNMENT,
        TokenTypes.EQUAL,
        TokenTypes.NOT_EQUAL,
        TokenTypes.LESS_THAN,
        TokenTypes.GREATER_THAN,
        TokenTypes.LESS_THAN_OR_EQUAL,
        TokenTypes.GREATER_THAN_OR_EQUAL,
        TokenTypes.AND,
        TokenTypes.OR,
        TokenTypes.NOT,
        TokenTypes.NUMBER_INTEGER,
        TokenTypes.NUMBER_REAL,
        TokenTypes.STRING,
        TokenTypes.ID,
        TokenTypes.MULTI_LINE_COMMENT,
        TokenTypes.SINGLE_LINE_COMMENT,
    )
    assert_tokens_sequence(tokens, delimeters_tokens)
