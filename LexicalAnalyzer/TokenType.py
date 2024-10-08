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
    TokenType('Whitesapce', r'( )'),
    TokenType('Tabulation', r'(\t)'),
    TokenType('Newline', r'(\n)'),
    TokenType('Semicolon', r'(;)'),
    TokenType('Сolon', r'(:)'),
    TokenType('Dot', r'(\.)'),
    TokenType('Comma', r'(,)'),
    TokenType('LeftBracket', r'(\()'),
    TokenType('RightBracket', r'(\))'),

    # keywords
    TokenType('Begin', r'(Begin)'),
    TokenType('End', r'(End)'),
    TokenType('Program', r'(Program)'),
    TokenType('Const', r'(Const)'),
    TokenType('Var', r'(Var)'),
    TokenType('FUNCTION', r'(FUNCTION)'),
    TokenType('PROCEDURE', r'(PROCEDURE)'),
    TokenType('ARRAY', r'(ARRAY)'),

    TokenType('Writeln', r'(Writeln)'),
    TokenType('Readln', r'(Readln)'),

    TokenType('If', r'(If)'),
    TokenType('Then', r'(Then)'),
    TokenType('Else', r'(Else)'),

    TokenType('For', r'(For)'),
    TokenType('While', r'(While)'),
    TokenType('To', r'(To)'),
    TokenType('Do', r'(Do)'),

    TokenType('True', r'(True)'),
    TokenType('False', r'(False)'),

    # data types
    TokenType('IntegerType', r'(Integer)'),
    TokenType('RealType', r'(Real)'),

    TokenType('StringType', r'(String)'),
    TokenType('CharType', r'(Char)'),

    TokenType('Boolean Type', r'(Boolean)'),

    # operators
    TokenType('Plus', r'(\+)'),
    TokenType('Minus', r'(-)'),
    TokenType('Multiply', r'(\*)'),
    TokenType('Division', r'(\))'),
    TokenType('Div', r'(div)'),
    TokenType('Mod', r'(mod)'),

    TokenType('Assignment', r'(:=)'),

    TokenType('Equal', r'(=)'),
    TokenType('NotEqual', r'(<>)'),
    TokenType('LessThan', r'(<)'),
    TokenType('GreaterThan', r'(>)'),
    TokenType('LessThanOrEqual', r'(<=)'),
    TokenType('GreaterThanOrEqual', r'(>=)'),

    TokenType('And', r'(And)'),
    TokenType('Or', r'(Or)'),
    TokenType('GreaterThanOrEqual', r'(Not)'),

    # ids
    TokenType('NumberInteger', r'(\d+)'),
    TokenType('NumberReal', r'(\d+\.\d+)'),
    TokenType('String', r"'(.*)'"),
    TokenType('Id', r'([a-zA-Z_]\w*)'),
    TokenType('SingleLineComment', r'\/\/(.*\n)'),
    TokenType('MultiLineComment', r'\{([^{}]*)\}'),
]


TOKEN_TYPES_LIST = {token_type.name: token_type for token_type in TOKEN_TYPES}
