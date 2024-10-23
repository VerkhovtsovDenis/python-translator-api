from LexicalAnalyzer import Lexer, FileManager


def parse_programm(programm):
    lexer = Lexer(code=programm)

    print('our code:')
    print('--------')
    print(programm)
    print('--------\n')
    print('Tokens:')

    for token in lexer.tokenize():
        print(token)


if __name__ == "__main__":
    path = r'\tests\lexer_code\1.pas'
    code = FileManager.get_code(relative_path=path)
    parse_programm(code)
