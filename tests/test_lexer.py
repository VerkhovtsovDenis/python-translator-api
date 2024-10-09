# flake8: noqa: F401
import pytest
from LexicalAnalyzer import Lexer, FileManager, TokenTypes

def test_can_lexer_init():
    path = r'C:\python\python-translator\tests\lexer_code\1.pas'
    pascal_code = FileManager.get_code(path)
    tokens = Lexer(code=pascal_code).tokenize()
    
def test_get_lexem_1pas():
    path = r'C:\python\python-translator\tests\lexer_code\1.pas'
    pascal_code = FileManager.get_code(path)
    tokens = Lexer(code=pascal_code).tokenize()
    print(tokens)
