class UnknowTokenError(Exception):
    UNKNOW_TOKEN_MESSEAGE = (
        "Syntax error, unknow token '{code}' found in line:{line}, pos:{pos}."
    )

    def __init__(self, code: str, line: int, pos: int):
        super().__init__(
            self.UNKNOW_TOKEN_MESSEAGE.format(code=code, line=line, pos=pos)
        )


class InvalidTokensError(Exception):
    INVALID_TOKENS_MESSEAGE = (
        "Syntax error, invalid tokens '{code}' found in line:{line}, pos:{pos}."
    )

    def __init__(self, code: str, line: int, pos: int):
        super().__init__(
            self.INVALID_TOKENS_MESSEAGE.format(code=code, line=line, pos=pos)
        )
