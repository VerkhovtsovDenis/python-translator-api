import pytest

from LexicalAnalyzer import Token, TokenTypes
from SemanticalAnalyzer.AST import (
    StatementsNode,
    ValueNode,
    VariableNode,
    BinaryOperatorNode,
    UnarOperatorNode,
)
from SemanticalAnalyzer.Variable import IntegerDataType


@pytest.fixture
def scope_integer_a_b_tokens() -> list[Token]:
    return (
        Token(token_type=TokenTypes.VAR),
        Token(token_type=TokenTypes.ID, value="a"),
        Token(token_type=TokenTypes.COMMA),
        Token(token_type=TokenTypes.ID, value="b"),
        Token(token_type=TokenTypes.COLON),
        Token(token_type=TokenTypes.INTEGER_TYPE),
        Token(token_type=TokenTypes.SEMICOLON),
    )


@pytest.fixture
def a_assignment_b_tokens() -> list[Token]:
    return (
        Token(token_type=TokenTypes.ID, value="a"),
        Token(token_type=TokenTypes.ASSIGNMENT),
        Token(token_type=TokenTypes.ID, value="b"),
        Token(token_type=TokenTypes.SEMICOLON),
    )


@pytest.fixture
def a_assignment_b_node() -> BinaryOperatorNode:
    left_operand = VariableNode(
        Token(token_type=TokenTypes.ID, value="a"), data_type=IntegerDataType
    )
    right_operand = VariableNode(
        Token(token_type=TokenTypes.ID, value="b"), data_type=IntegerDataType
    )
    assignment_node = BinaryOperatorNode(
        Token(token_type=TokenTypes.ASSIGNMENT), left_operand, right_operand
    )
    return assignment_node


@pytest.fixture
def a_assignment_12_tokens() -> list[Token]:
    return (
        Token(token_type=TokenTypes.ID, value="a"),
        Token(token_type=TokenTypes.ASSIGNMENT),
        Token(token_type=TokenTypes.NUMBER_INTEGER, value="12"),
        Token(token_type=TokenTypes.SEMICOLON),
    )


@pytest.fixture
def a_assignment_12_node() -> BinaryOperatorNode:
    left_operand = VariableNode(
        Token(token_type=TokenTypes.ID, value="a"), data_type=IntegerDataType
    )
    right_operand = ValueNode(
        Token(token_type=TokenTypes.NUMBER_INTEGER, value="12"),
        data_type=IntegerDataType,
    )
    assignment_node = BinaryOperatorNode(
        Token(token_type=TokenTypes.ASSIGNMENT), left_operand, right_operand
    )
    return assignment_node


@pytest.fixture
def a_assignment_12_with_brackets_tokens() -> list[Token]:
    return (
        Token(token_type=TokenTypes.ID, value="a"),
        Token(token_type=TokenTypes.ASSIGNMENT),
        Token(token_type=TokenTypes.LEFT_BRACKET),
        Token(token_type=TokenTypes.NUMBER_INTEGER, value="12"),
        Token(token_type=TokenTypes.RIGHT_BRACKET),
        Token(token_type=TokenTypes.SEMICOLON),
    )


@pytest.fixture
def a_assignment_12_with_many_brackets_tokens() -> list[Token]:
    return (
        Token(token_type=TokenTypes.ID, value="a"),
        Token(token_type=TokenTypes.ASSIGNMENT),
        Token(token_type=TokenTypes.LEFT_BRACKET),
        Token(token_type=TokenTypes.LEFT_BRACKET),
        Token(token_type=TokenTypes.NUMBER_INTEGER, value="12"),
        Token(token_type=TokenTypes.RIGHT_BRACKET),
        Token(token_type=TokenTypes.RIGHT_BRACKET),
        Token(token_type=TokenTypes.SEMICOLON),
    )


@pytest.fixture
def a_b_difficult_fomula() -> list[Token]:
    return (
        Token(token_type=TokenTypes.ID, value="a"),
        Token(token_type=TokenTypes.ASSIGNMENT),
        Token(token_type=TokenTypes.NUMBER_INTEGER, value="12"),
        Token(token_type=TokenTypes.PLUS),
        Token(token_type=TokenTypes.NUMBER_INTEGER, value="10"),
        Token(token_type=TokenTypes.MULTIPLY),
        Token(token_type=TokenTypes.ID, value="b"),
        Token(token_type=TokenTypes.SEMICOLON),
    )


@pytest.fixture
def a_b_difficult_fomula_node() -> BinaryOperatorNode:
    left_operand = VariableNode(
        Token(token_type=TokenTypes.ID, value="a"), data_type=IntegerDataType
    )
    right_operand = BinaryOperatorNode(
        Token(token_type=TokenTypes.MULTIPLY),
        BinaryOperatorNode(
            Token(token_type=TokenTypes.PLUS),
            ValueNode(
                Token(token_type=TokenTypes.NUMBER_INTEGER, value="12"),
                data_type=IntegerDataType,
            ),
            ValueNode(
                Token(token_type=TokenTypes.NUMBER_INTEGER, value="10"),
                data_type=IntegerDataType,
            ),
        ),
        VariableNode(
            Token(token_type=TokenTypes.ID, value="b"), data_type=IntegerDataType
        ),
    )
    assignment_node = BinaryOperatorNode(
        Token(token_type=TokenTypes.ASSIGNMENT), left_operand, right_operand
    )
    return assignment_node
