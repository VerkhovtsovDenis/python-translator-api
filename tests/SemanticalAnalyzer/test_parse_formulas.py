import pytest

from SemanticalAnalyzer.AST import (
    StatementsNode,
)
from tests.utils import emulate_tokens_generator
from LexicalAnalyzer import Token, TokenTypes
from SemanticalAnalyzer import (
    Parser,
    UnknowIdError,
    TypeError,
    UnExpectedTokenError,
)


def assert_ast_by_tokens(input_tokens: list[Token], expected_ast: StatementsNode):
    tokens_genarator = emulate_tokens_generator(input_tokens)
    parser = Parser(tokens_genarator)
    actual_ast = parser.parse_code()
    assert actual_ast == expected_ast


def test_unknow_id_raise():
    tokens = (
        Token(token_type=TokenTypes.BEGIN),
        Token(token_type=TokenTypes.ID, value="a"),
        Token(token_type=TokenTypes.ASSIGNMENT),
        Token(token_type=TokenTypes.NUMBER_INTEGER, value="12"),
        Token(token_type=TokenTypes.SEMICOLON),
        Token(token_type=TokenTypes.END),
        Token(token_type=TokenTypes.DOT),
    )
    tokens_genarator = emulate_tokens_generator(tokens)
    with pytest.raises(UnknowIdError):
        parser = Parser(tokens_genarator)
        parser.parse_code()
        assert parser._global_scope == {}


def test_type_error_raise(scope_integer_a_b_tokens):
    tokens = scope_integer_a_b_tokens + (
        Token(token_type=TokenTypes.BEGIN),
        Token(token_type=TokenTypes.ID, value="a"),
        Token(token_type=TokenTypes.ASSIGNMENT),
        Token(token_type=TokenTypes.STRING, value="'str'"),
        Token(token_type=TokenTypes.SEMICOLON),
        Token(token_type=TokenTypes.END),
        Token(token_type=TokenTypes.DOT),
    )
    tokens_genarator = emulate_tokens_generator(tokens)
    with pytest.raises(TypeError):
        parser = Parser(tokens_genarator)
        parser.parse_code()


@pytest.mark.parametrize(
    "code_tokens",
    [
        pytest.param(
            (
                Token(token_type=TokenTypes.BEGIN),
                Token(token_type=TokenTypes.ID, value="a"),
                Token(token_type=TokenTypes.ASSIGNMENT),
                Token(token_type=TokenTypes.ASSIGNMENT),
                Token(token_type=TokenTypes.SEMICOLON),
                Token(token_type=TokenTypes.END),
                Token(token_type=TokenTypes.DOT),
            ),
            id="Double assignment",
        ),
        pytest.param(
            (
                Token(token_type=TokenTypes.BEGIN),
                Token(token_type=TokenTypes.ID, value="a"),
                Token(token_type=TokenTypes.ASSIGNMENT),
                Token(token_type=TokenTypes.LEFT_BRACKET, value="a"),
                Token(token_type=TokenTypes.ID, value="a"),
                Token(token_type=TokenTypes.SEMICOLON),
                Token(token_type=TokenTypes.END),
                Token(token_type=TokenTypes.DOT),
            ),
            id="Assignment with unbound bracket",
        ),
        pytest.param(
            (
                Token(token_type=TokenTypes.BEGIN),
                Token(token_type=TokenTypes.ID, value="a"),
                Token(token_type=TokenTypes.ASSIGNMENT),
                Token(token_type=TokenTypes.ID, value="a"),
                Token(token_type=TokenTypes.SEMICOLON),
                Token(token_type=TokenTypes.END),
                Token(token_type=TokenTypes.SEMICOLON),
            ),
            id="Assignment without end dot",
        ),
    ],
)
def test_type_unexpected_token(code_tokens, scope_integer_a_b_tokens):
    tokens = scope_integer_a_b_tokens + code_tokens
    tokens_genarator = emulate_tokens_generator(tokens)
    with pytest.raises(UnExpectedTokenError):
        parser = Parser(tokens_genarator)
        parser.parse_code()


def test_assignment_with_formula_with_two_varibles(
    scope_integer_a_b_tokens,
    a_scope_node,
    b_scope_node,
    a_assignment_b_tokens,
    a_assignment_b_node,
):
    tokens = (
        scope_integer_a_b_tokens
        + (Token(token_type=TokenTypes.BEGIN),)
        + a_assignment_b_tokens
        + (
            Token(token_type=TokenTypes.END),
            Token(token_type=TokenTypes.DOT),
        )
    )

    expected_ast = StatementsNode()
    expected_ast.add_node(a_scope_node)
    expected_ast.add_node(b_scope_node)

    programm_node = StatementsNode()
    programm_node.add_node(a_assignment_b_node)
    expected_ast.add_node(programm_node)

    assert_ast_by_tokens(tokens, expected_ast)


def test_assignment_with_formula_with_varibale_and_value(
    scope_integer_a_b_tokens,
    a_scope_node,
    b_scope_node,
    a_assignment_12_tokens,
    a_assignment_12_node,
):
    tokens = (
        scope_integer_a_b_tokens
        + (Token(token_type=TokenTypes.BEGIN),)
        + a_assignment_12_tokens
        + (
            Token(token_type=TokenTypes.END),
            Token(token_type=TokenTypes.DOT),
        )
    )

    expected_ast = StatementsNode()
    expected_ast.add_node(a_scope_node)
    expected_ast.add_node(b_scope_node)
    programm_node = StatementsNode()
    programm_node.add_node(a_assignment_12_node)
    expected_ast.add_node(programm_node)

    assert_ast_by_tokens(tokens, expected_ast)


def test_two_assignment_test(
    scope_integer_a_b_tokens,
    a_scope_node,
    b_scope_node,
    a_assignment_b_tokens,
    a_assignment_b_node,
    a_assignment_12_tokens,
    a_assignment_12_node,
):
    tokens = (
        scope_integer_a_b_tokens
        + (Token(token_type=TokenTypes.BEGIN),)
        + a_assignment_b_tokens
        + a_assignment_12_tokens
        + (
            Token(token_type=TokenTypes.END),
            Token(token_type=TokenTypes.DOT),
        )
    )

    expected_ast = StatementsNode()
    expected_ast.add_node(a_scope_node)
    expected_ast.add_node(b_scope_node)
    programm_node = StatementsNode()
    programm_node.add_node(a_assignment_b_node)
    programm_node.add_node(a_assignment_12_node)
    expected_ast.add_node(programm_node)

    assert_ast_by_tokens(tokens, expected_ast)


def test_assignment_with_brackets(
    scope_integer_a_b_tokens,
    a_scope_node,
    b_scope_node,
    a_assignment_12_with_brackets_tokens,
    a_assignment_12_node,
):
    tokens = (
        scope_integer_a_b_tokens
        + (Token(token_type=TokenTypes.BEGIN),)
        + a_assignment_12_with_brackets_tokens
        + (
            Token(token_type=TokenTypes.END),
            Token(token_type=TokenTypes.DOT),
        )
    )

    expected_ast = StatementsNode()
    expected_ast.add_node(a_scope_node)
    expected_ast.add_node(b_scope_node)
    programm_node = StatementsNode()
    programm_node.add_node(a_assignment_12_node)
    expected_ast.add_node(programm_node)

    assert_ast_by_tokens(tokens, expected_ast)


def test_assignment_with_many_brackets(
    scope_integer_a_b_tokens,
    a_scope_node,
    b_scope_node,
    a_assignment_12_with_many_brackets_tokens,
    a_assignment_12_node,
):
    tokens = (
        scope_integer_a_b_tokens
        + (Token(token_type=TokenTypes.BEGIN),)
        + a_assignment_12_with_many_brackets_tokens
        + (
            Token(token_type=TokenTypes.END),
            Token(token_type=TokenTypes.DOT),
        )
    )

    expected_ast = StatementsNode()
    expected_ast.add_node(a_scope_node)
    expected_ast.add_node(b_scope_node)
    programm_node = StatementsNode()
    programm_node.add_node(a_assignment_12_node)
    expected_ast.add_node(programm_node)

    assert_ast_by_tokens(tokens, expected_ast)


def test_difficult_formula(
    scope_integer_a_b_tokens,
    a_scope_node,
    b_scope_node,
    a_b_difficult_fomula,
    a_b_difficult_fomula_node,
):
    tokens = (
        scope_integer_a_b_tokens
        + (Token(token_type=TokenTypes.BEGIN),)
        + a_b_difficult_fomula
        + (
            Token(token_type=TokenTypes.END),
            Token(token_type=TokenTypes.DOT),
        )
    )

    expected_ast = StatementsNode()
    expected_ast.add_node(a_scope_node)
    expected_ast.add_node(b_scope_node)
    programm_node = StatementsNode()
    programm_node.add_node(a_b_difficult_fomula_node)
    expected_ast.add_node(programm_node)

    assert_ast_by_tokens(tokens, expected_ast)
