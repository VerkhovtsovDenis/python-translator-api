# flake8: noqa: F401
import pytest

from LexicalAnalyzer import Lexer, TokenTypes, InvalidTokensError, UnknowTokenError


def assert_tokens_sequence(actual_sequence, expected_sequence):
    for token, corrett_token_type in zip(actual_sequence, expected_sequence):
        assert token.token_type == corrett_token_type


def test_can_lexer_init():
    pascal_code = """writeln('Привет, мир!');"""

    tokens = Lexer(code=pascal_code).tokenize()
    assert tokens is not None


def test_get_lexem_simple_programm():
    pascal_code = """
    begin
        writeln('Привет, мир!'); // однострочный комментарий
    end.
    """
    actaul_tokens = Lexer(code=pascal_code).tokenize()

    expected_tokens = [
        TokenTypes.BEGIN,
        TokenTypes.WRITELN,
        TokenTypes.LEFT_BRACKET,
        TokenTypes.STRING,
        TokenTypes.RIGHT_BRACKET,
        TokenTypes.SEMICOLON,
        TokenTypes.END,
        TokenTypes.DOT,
    ]

    assert_tokens_sequence(actaul_tokens, expected_tokens)


def test_get_lexem_hard_programm():
    pascal_code = """
    var
        a,b: real;
        r: real;
    begin
        {
            многостройчный
            комментарий
        }
        write('Введите координату точки a: ');
        readln(a);
        a := 123.4
        write('Введите координату точки b: ');
        readln(b);
        r := abs(a-b);
        writeln('Расстояние между точками = ', r);
    end.
    """
    actaul_tokens = Lexer(code=pascal_code).tokenize()

    expected_tokens = [
        TokenTypes.VAR,
        TokenTypes.ID,
        TokenTypes.COMMA,
        TokenTypes.ID,
        TokenTypes.COLON,
        TokenTypes.REAL_TYPE,
        TokenTypes.SEMICOLON,
        TokenTypes.ID,
        TokenTypes.COLON,
        TokenTypes.REAL_TYPE,
        TokenTypes.SEMICOLON,
        TokenTypes.BEGIN,
        # строка 9
        TokenTypes.WRITE,
        TokenTypes.LEFT_BRACKET,
        TokenTypes.STRING,
        TokenTypes.RIGHT_BRACKET,
        TokenTypes.SEMICOLON,
        TokenTypes.READLN,
        TokenTypes.LEFT_BRACKET,
        TokenTypes.ID,
        TokenTypes.RIGHT_BRACKET,
        TokenTypes.SEMICOLON,
        TokenTypes.ID,
        TokenTypes.ASSIGNMENT,
        TokenTypes.NUMBER_REAL,
        # строка 12
        TokenTypes.WRITE,
        TokenTypes.LEFT_BRACKET,
        TokenTypes.STRING,
        TokenTypes.RIGHT_BRACKET,
        TokenTypes.SEMICOLON,
        TokenTypes.READLN,
        TokenTypes.LEFT_BRACKET,
        TokenTypes.ID,
        TokenTypes.RIGHT_BRACKET,
        TokenTypes.SEMICOLON,
        TokenTypes.ID,
        TokenTypes.ASSIGNMENT,
        TokenTypes.ID,
        TokenTypes.LEFT_BRACKET,
        TokenTypes.ID,
        TokenTypes.MINUS,
        TokenTypes.ID,
        TokenTypes.RIGHT_BRACKET,
        TokenTypes.SEMICOLON,
        # строка 15
        TokenTypes.WRITELN,
        TokenTypes.LEFT_BRACKET,
        TokenTypes.STRING,
        TokenTypes.COMMA,
        TokenTypes.ID,
        TokenTypes.RIGHT_BRACKET,
        TokenTypes.SEMICOLON,
        # строка 16
        TokenTypes.END,
        TokenTypes.DOT,
    ]

    assert_tokens_sequence(actaul_tokens, expected_tokens)


@pytest.mark.parametrize(
    ("pascal_code"),
    (
        ("^"),
        ("begin ^"),
        ("^ begin"),
        ("begin^"),
    ),
)
def test_raise_lexic_error_when_unknow_token(pascal_code):
    with pytest.raises(UnknowTokenError):
        list(Lexer(code=pascal_code).tokenize())


@pytest.mark.parametrize(
    ("pascal_code"),
    (("124.3p"), ("123d"), ("'sdf'f"), ("'fds'1")),
)
def test_raise_lexic_error_when_invalid_tokens(pascal_code):
    with pytest.raises(InvalidTokensError):
        list(Lexer(code=pascal_code).tokenize())
