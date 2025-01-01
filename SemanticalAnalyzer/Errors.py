from LexicalAnalyzer import TokenType


class RedeceredIdError(Exception):
    MESSAGE = "Semantic error, Re-declared identifier '{id}'."

    def __init__(self, id: str):
        super().__init__(self.MESSAGE.format(id=id))


class UnExpectedTokenError(Exception):
    MESSAGE = (
        "Semantic error, expected in {expected_tokens}, "
        "but actual {actual_token} in line:{line}, pos:{pos}."
    )

    def __init__(
        self,
        expected_tokens: list[TokenType],
        actual_token: TokenType,
        line: int,
        pos: int,
    ):
        super().__init__(
            self.MESSAGE.format(
                expected_tokens=expected_tokens,
                actual_token=actual_token,
                line=line,
                pos=pos,
            )
        )


class TypeError(Exception):
    MESSAGE = (
        "Type error, token '{code}' in line:{line}, pos:{pos}, "
        "must be type {expected_type}."
    )

    def __init__(
        self,
        code: str,
        expected_type: str,
        line: int,
        pos: int,
    ):
        super().__init__(
            self.MESSAGE.format(
                code=code,
                expected_type=expected_type,
                line=line,
                pos=pos,
            )
        )


class UnknowIdError(Exception):
    MESSAGE = "Unknow identifier error, identifier '{code}' in line:{line}, pos:{pos} not found."

    def __init__(
        self,
        code: str,
        line: int,
        pos: int,
    ):
        super().__init__(
            self.MESSAGE.format(
                code=code,
                line=line,
                pos=pos,
            )
        )
