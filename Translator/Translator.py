from LexicalAnalyzer import Lexer
from SemanticalAnalyzer import Parser
from CodeGenerator import Generator
from constants import SupportLanguages


class Translator:

    @classmethod
    def pascal_translate(self, pascal_code: str, target_language: SupportLanguages):
        lexer = Lexer(code=pascal_code)
        tokens_gen = lexer.tokenize()
        parser = Parser(tokens_gen)

        # ast можем хешировать и не считать каждый раз
        ast = parser.parse_code()
        gen = Generator(ast)
        return gen.generate(target_language)
