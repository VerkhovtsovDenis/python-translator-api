from .TokenType import TokenType


class Token:
    def __init__(self, *, token_type: TokenType, string, value, line, pos):

        self.token_type = token_type

        # to understand why we create both string and value see example
        self.string = string  # example '"Привет мир!"'
        self.value = value  # example 'Привет мир!'

        self.line = line
        self.pos = pos

    def __str__(self):
        return (f'token: {self.token_type.name}, value: {repr(self.value)}'
                f' in line: {self.line+1}, pos: {self.pos+1}')
