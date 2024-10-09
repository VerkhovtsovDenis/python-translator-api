from LexicalAnalyzer import Lexer, FileManager
from LexicalAnalyzer.TokenType import TOKEN_TYPES_LIST


def parse_programm(programm):
    lexer = Lexer(code=programm)

    ignore_tokens = (
        TOKEN_TYPES_LIST.get('Newline'),
        TOKEN_TYPES_LIST.get('Whitesapce'),
        TOKEN_TYPES_LIST.get('Tabulation'),
    )

    print('our code:')
    print('--------')
    print(programm)
    print('--------\n')
    print('Tokens:')

    for token in lexer.tokenize():
        if token.token_type not in ignore_tokens:
            print(token)


if __name__ == "__main__":
    path = r'C:\python\python-translator\tests\lexer_code\1.pas'
    code = FileManager.get_code(filepath=path)
    parse_programm(code)
