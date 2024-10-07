class TokenType:
    def __init__(self, name, regex):
        self.name = name
        self.regex = regex


# regular expressions can create in any case
# it ignore in Lexer

# preference is always given to the longest occurrence
# if length is equal, preference is given tofirst in TOKEN_TYPES_LIST

TOKEN_TYPES_LIST = {
    # delimeters
    'Whitesapce': TokenType('Whitesapce', r' '),
    'Tabulation': TokenType('Tabulation', r'\t'),
    'Newline': TokenType('Newline', r'\n'),
    'Semicolon': TokenType('Semicolon', r';'),
    'Сolon': TokenType('Сolon', r':'),
    'Dot': TokenType('Dot', r'\.'),
    'Comma': TokenType('Comma', r','),
    'Quotation Mark': TokenType('Quotation Mark', r"'"),
    'Left Bracket': TokenType('Left Bracket', r'\('),
    'Right Bracket': TokenType('Right Bracket', r'\)'),

    # keywords
    'Begin': TokenType('Begin', r'Begin'),
    'End': TokenType('End', r'End'),
    'Program': TokenType('Program', r'Program'),
    'Const': TokenType('Const', r'Const'),
    'Var': TokenType('Var', r'Var'),

    'Writeln': TokenType('Writeln', r'Writeln'),
    'Readln': TokenType('Readln', r'Readln'),

    'If': TokenType('If', r'If'),
    'Then': TokenType('Then', r'Then'),
    'Else': TokenType('Else', r'Else'),

    'For': TokenType('For', r'For'),
    'While': TokenType('For', r'For'),
    'To': TokenType('To', r'To'),
    'Do': TokenType('Do', r'Do'),

    'True': TokenType('True', r'True'),
    'False': TokenType('False', r'False'),

    # data types
    'Integer Type': TokenType('Integer Type', r'Integer'),
    'Real Type': TokenType('Real Type', r'Real'),

    'String Type': TokenType('String Type', r'String'),
    'Char Type': TokenType('Char Type', r'Char'),

    'Boolean Type': TokenType('Boolean Type', r'Boolean'),

    # operators
    'Plus': TokenType('Plus', r'\+'),
    'Minus': TokenType('Minus', r'-'),
    'Multiply': TokenType('Multiply', r'\*'),
    'Division': TokenType('Division', r'/'),
    'Div': TokenType('Div', r'div'),
    'Mod': TokenType('Mod', r'mod'),

    'Assignment': TokenType('Assignment', r':='),

    'Equal': TokenType('Equal', r'='),
    'Not Equal': TokenType('Not Equal ', r'<>'),
    'Less Than': TokenType('Less Than ', r'<'),
    'Greater Than': TokenType('Greater Than', r'>'),
    'Less Than Or Equal': TokenType('Less Than Or Equal', r'<='),
    'Greater Than Or Equal': TokenType('Greater Than Or Equal', r'>='),

    'And': TokenType('And', r'And'),
    'Or': TokenType('Or', r'Or'),
    'Not': TokenType('Greater Than Or Equal', r'Not'),

    # ids
    'Number': TokenType('Number', r'(\d+)(.(\d+))?'),
    'String': TokenType('String', r"'.*'"),
    'Id': TokenType('Id', r'[a-zA-Z_]\w*'),
}
