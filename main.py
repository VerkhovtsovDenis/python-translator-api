import sys
from LexicalAnalyzer import Lexer
from SemanticalAnalyzer import Parser
from CodeGenerator import Generator


def parse_programm(programm):
    lexer = Lexer(code=programm)
    parser = Parser(lexer.tokenize())
    tree = parser.parse_code()
    gen = Generator(tree)
    python_code = gen.generate()
    print(python_code)


if __name__ == "__main__":
    code = """
    program hello;
    var a, b: Integer;
    begin
        b:=1;
        write(b,1,3);
    end.
    """
    parse_programm(code)
