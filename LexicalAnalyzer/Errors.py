class LexicError(Exception):
    pass


INVALID_TOKENS_MESSEAGE = (
    "Syntax error, invalid tokens '{code}' found in line:{line}, pos:{pos}."
)

UNKNOW_TOKEN_MESSEAGE = (
    "Syntax error, unknow token '{code}' found in line:{line}, pos:{pos}."
)
