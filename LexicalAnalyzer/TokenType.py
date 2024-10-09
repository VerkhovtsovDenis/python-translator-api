from enum import Enum


class TokenType:
    def __init__(self, name, regex):
        self.name = name
        self.regex = regex

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<TokenType(name={self.name}, regex={self.regex})>"


class TokenTypes(Enum):
    # delimeters
    COLON = TokenType('colon', r'(:)')
    DOT = TokenType('dot', r'(\.)')
    COMMA = TokenType('comma', r'(,)')
    LEFT_BRACKET = TokenType('left_bracket', r'(\()')
    RIGHT_BRACKET = TokenType('right_bracket', r'(\))')
    WHITESPACE = TokenType('whitespace', r'( )')
    TABULATION = TokenType('tabulation', r'(\t)')
    NEWLINE = TokenType('newline', r'(\n)')
    SEMICOLON = TokenType('semicolon', r'(;)')

    # keywords
    BEGIN = TokenType('begin', r'(Begin)')
    END = TokenType('end', r'(End)')
    PROGRAM = TokenType('program', r'(Program)')
    CONST = TokenType('const', r'(Const)')
    VAR = TokenType('var', r'(Var)')
    FUNCTION = TokenType('function', r'(FUNCTION)')
    PROCEDURE = TokenType('procedure', r'(PROCEDURE)')
    ARRAY = TokenType('array', r'(ARRAY)')

    WRITELN = TokenType('writeln', r'(Writeln)')
    READLN = TokenType('readln', r'(Readln)')

    IF = TokenType('if', r'(If)')
    THEN = TokenType('then', r'(Then)')
    ELSE = TokenType('else', r'(Else)')

    FOR = TokenType('for', r'(For)')
    WHILE = TokenType('while', r'(While)')
    TO = TokenType('to', r'(To)')
    DO = TokenType('do', r'(Do)')

    TRUE = TokenType('true', r'(True)')
    FALSE = TokenType('false', r'(False)')

    # data types
    INTEGER_TYPE = TokenType('integer_type', r'(Integer)')
    REAL_TYPE = TokenType('real_type', r'(Real)')

    STRING_TYPE = TokenType('string_type', r'(String)')
    CHAR_TYPE = TokenType('char_type', r'(Char)')

    BOOLEAN_TYPE = TokenType('boolean_type', r'(Boolean)')

    # operators
    PLUS = TokenType('plus', r'(\+)')
    MINUS = TokenType('minus', r'(-)')
    MULTIPLY = TokenType('multiply', r'(\*)')
    DIVISION = TokenType('division', r'(\/)')
    DIV = TokenType('div', r'(div)')
    MOD = TokenType('mod', r'(mod)')

    ASSIGNMENT = TokenType('assignment', r'(:=)')

    EQUAL = TokenType('equal', r'(=)')
    NOT_EQUAL = TokenType('not_equal', r'(<>)')
    LESS_THAN = TokenType('less_than', r'(<)')
    GREATER_THAN = TokenType('greater_than', r'(>)')
    LESS_THAN_OR_EQUAL = TokenType('less_than_or_equal', r'(<=)')
    GREATER_THAN_OR_EQUAL = TokenType('greater_than_or_equal', r'(>=)')

    AND = TokenType('and', r'(And)')
    OR = TokenType('or', r'(Or)')
    NOT = TokenType('not', r'(Not)')

    # ids
    NUMBER_INTEGER = TokenType('number_integer', r'(\d+)')
    NUMBER_REAL = TokenType('number_real', r'(\d+\.\d+)')
    STRING = TokenType('string', r"'(.*)'")
    ID = TokenType('id', r'([a-zA-Z_]\w*)')
    SINGLE_LINE_COMMENT = TokenType('single_line_comment', r'\/\/(.*\n)')
    MULTI_LINE_COMMENT = TokenType('multi_line_comment', r'\{([^{}]*)\}')

    def __str__(self):
        return str(self.value.name)  # При вызове str(TokenTypes.WHITESPACE)
        # будет возвращено 'whitespace'

    # def __getattr__(self, attr):
    #     return getattr(self.value, attr)
