from .TokenType import TokenType


class Token:
    def __init__(self, token_type: TokenType, value, line, pos):

        self.token_type = token_type
        self.value = value
        self.line = line
        self.pos = pos

    def __str__(self):
        return (f'token: {self.token_type.name}, value: {repr(self.value)}'
                f' in line: {self.line+1}, pos: {self.pos+1}')
