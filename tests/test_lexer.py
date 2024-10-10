# flake8: noqa: F401
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from LexicalAnalyzer import Lexer, FileManager, TokenTypes

def test_can_lexer_init():
    path = r'\tests\lexer_code\1.pas'
    pascal_code = FileManager.get_code(path)
    tokens = Lexer(code=pascal_code).tokenize()
    
def test_get_lexem_1pas():
    path = r'\tests\lexer_code\1.pas'
    pascal_code = FileManager.get_code(path)
    tokens = list(Lexer(code=pascal_code).tokenize())
    delimeters_tokens = tokens

    correct_tokens_subsequence = [
        TokenTypes.WHITESPACE,
        TokenTypes.BEGIN,
        TokenTypes.NEWLINE,
        TokenTypes.WHITESPACE,
        TokenTypes.WRITELN,
        TokenTypes.LEFT_BRACKET,
        TokenTypes.STRING,
        TokenTypes.RIGHT_BRACKET, 
        TokenTypes.SEMICOLON,
        TokenTypes.WHITESPACE,
        TokenTypes.SINGLE_LINE_COMMENT,
        TokenTypes.WHITESPACE, 
        TokenTypes.END,
        TokenTypes.DOT
    ]

    for token, corrett_token_type in zip(delimeters_tokens, correct_tokens_subsequence):
        assert token.token_type == corrett_token_type

def test_get_lexem_2pas():
    path = r'\tests\lexer_code\1.pas'
    pascal_code = FileManager.get_code(path)
    tokens = list(Lexer(code=pascal_code).tokenize())
    delimeters_tokens = tokens

    correct_tokens_subsequence = [
        TokenTypes.WHITESPACE,
        TokenTypes.BEGIN,
        TokenTypes.NEWLINE,
        TokenTypes.WHITESPACE,
        TokenTypes.WRITELN,
        TokenTypes.LEFT_BRACKET,
        TokenTypes.STRING,
        TokenTypes.RIGHT_BRACKET, 
        TokenTypes.SEMICOLON,
        TokenTypes.WHITESPACE,
        TokenTypes.SINGLE_LINE_COMMENT,
        TokenTypes.WHITESPACE, 
        TokenTypes.END,
        TokenTypes.DOT
    ]

    for token, corrett_token_type in zip(delimeters_tokens, correct_tokens_subsequence):
        assert token.token_type == corrett_token_type


if __name__ == "__main__":
    test_get_lexem_1pas()
    