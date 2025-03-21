from .TokenType import TokenType


class Token:

    def __init__(
        self,
        *,
        token_type: TokenType,
        string: str = "",
        value: str = "",
        line: int = 0,
        pos: int = 0,
    ):

        self.token_type = token_type

        # to understand why we create both string and value see example
        self.string = string  # example '"Привет мир!"'
        self.value = value  # example 'Привет мир!'

        self.line = line
        self.pos = pos

    def __eq__(self, value):
        return (
            isinstance(value, Token)
            and self.token_type == value.token_type
            and self.value == value.value
        )

    def __str__(self):
        return (
            f"token: {self.token_type.name}, value: {repr(self.value)}"
            f" in line: {self.line+1}, pos: {self.pos+1}"
        )

    def __repr__(self):
        return f"<Token(value={self.value}, regex={self.token_type}, \
line={self.line}, pos={self.pos})>"
