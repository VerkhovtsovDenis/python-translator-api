from LexicalAnalyzer import Token


def emulate_tokens_generator(tokens: list[Token]):
    for token in tokens:
        yield token
