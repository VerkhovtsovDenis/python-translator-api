from LexicalAnalyzer import Lexer
from LexicalAnalyzer.TokenType import TOKEN_TYPES_LIST

example_programms = [
    '''
    begin
        writeln('Привет, мир!');
    end.
    ''',

    '''
    var
        a,b: real;
        r: real;
    begin
        write('Введите координату точки a: ');
        readln(a);
        a := 123.4
        write('Введите координату точки b: ');
        readln(b);
        r := abs(a-b);
        writeln('Расстояние между точками = ', r);
    end.
    ''',
]


def parse_programm(programm):
    lexer = Lexer(inpt=programm)
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
    [parse_programm(programm) for programm in example_programms]
