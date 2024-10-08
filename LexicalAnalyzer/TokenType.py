from collections import namedtuple


class TokenType:
    def __init__(self, name, regex):
        self.name = name
        self.regex = regex


# regular expressions can create in any case
# it ignore in Lexer
# token string must be in the 0 group
# token value must be in the 1 group


# preference is always given to the longest occurrence
# if length is equal, preference is given tofirst in TOKEN_TYPES_LIST

TOKEN_TYPES = [
    # delimeters
    TokenType('whitesapce_token', r'( )'),
    TokenType('tabulation_token', r'(\t)'),
    TokenType('newline_token', r'(\n)'),
    TokenType('semicolon_token', r'(;)'),
    TokenType('colon_token', r'(:)'),
    TokenType('dot_token', r'(\.)'),
    TokenType('comma_token', r'(,)'),
    TokenType('left_bracket_token', r'(\()'),
    TokenType('right_bracket_token', r'(\))'),

    # keywords
    TokenType('begin_token', r'(Begin)'),
    TokenType('end_token', r'(End)'),
    TokenType('program_token', r'(Program)'),
    TokenType('const_token', r'(Const)'),
    TokenType('var_token', r'(Var)'),
    TokenType('function_token', r'(FUNCTION)'),
    TokenType('procedure_token', r'(PROCEDURE)'),
    TokenType('array_token', r'(ARRAY)'),

    TokenType('writeln_token', r'(Writeln)'),
    TokenType('readln_token', r'(Readln)'),

    TokenType('if_token', r'(If)'),
    TokenType('then_token', r'(Then)'),
    TokenType('else_token', r'(Else)'),

    TokenType('for_token', r'(For)'),
    TokenType('while_token', r'(While)'),
    TokenType('to_token', r'(To)'),
    TokenType('do_token', r'(Do)'),

    TokenType('true_token', r'(True)'),
    TokenType('false_token', r'(False)'),

    # data types
    TokenType('integer_type_token', r'(Integer)'),
    TokenType('real_type_token', r'(Real)'),

    TokenType('string_type_token', r'(String)'),
    TokenType('char_type_token', r'(Char)'),

    TokenType('boolean_type_token', r'(Boolean)'),

    # operators
    TokenType('plus_token', r'(\+)'),
    TokenType('minus_token', r'(-)'),
    TokenType('multiply_token', r'(\*)'),
    TokenType('division_token', r'(\))'),
    TokenType('div_token', r'(div)'),
    TokenType('mod_token', r'(mod)'),

    TokenType('assignment_token', r'(:=)'),

    TokenType('equal_token', r'(=)'),
    TokenType('not_equal_token', r'(<>)'),
    TokenType('less_than_token', r'(<)'),
    TokenType('greater_than_token', r'(>)'),
    TokenType('less_than_or_equal_token', r'(<=)'),
    TokenType('greater_than_or_equal_token', r'(>=)'),

    TokenType('and_token', r'(And)'),
    TokenType('or_token', r'(Or)'),
    TokenType('not_token', r'(Not)'),

    # ids
    TokenType('number_integer_token', r'(\d+)'),
    TokenType('number_real_token', r'(\d+\.\d+)'),
    TokenType('string_token', r"'(.*)'"),
    TokenType('id_token', r'([a-zA-Z_]\w*)'),
    TokenType('single_line_comment_token', r'\/\/(.*\n)'),
    TokenType('multi_line_comment_token', r'\{([^{}]*)\}'),
]

Tokens = namedtuple('Tokens', list(map(lambda x: x.name, TOKEN_TYPES)))

TOKEN_TYPES_LIST = Tokens(*TOKEN_TYPES)