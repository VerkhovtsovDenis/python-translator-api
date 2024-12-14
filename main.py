from LexicalAnalyzer import Lexer
from SemanticalAnalyzer import Parser
from FileManager import FileManager


def parse_programm(programm):
    lexer = Lexer(code=programm)

    print("our code:")
    print("--------")
    print(programm)
    print("--------\n")
    print("Tokens:")

    [print(token) for token in lexer.tokenize()]

    parser = Parser(lexer.tokenize())

    # tree = parser.parse_code()
    # print(tree)


if __name__ == "__main__":
    # path = r"\tests\lexer_code\1.pas"
    # code = FileManager.get_code(relative_path=path)
    code = """
    123f
    """
    parse_programm(code)
