from LexicalAnalyzer import Lexer
from LexicalAnalyzer.TokenType import TOKEN_TYPES_LIST

example_programms = [
    r'''
    begin
        writeln('Привет, мир!'); // однострочный комментарий
    end.
    ''',

    r'''
    var
        a,b: real;
        r: real;
    begin
        {
            многостройчный
            комментарий
        }
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

example_programms_with_errors = [
    r'''
    123x
    { это неправильная запись числа, но считает ее как два токена
      number integer и id }
    ''',

    r'''
    124..
    { это неправильная запись числа, но считает ее как три токена
      number integer и два dot }
    ''',

    r'''
    124.3p
    { это неправильная запись числа, но считает ее как два токена
      number real и id }
    ''',

    r'''
    function(a
    // не хватающие скобки в теории тоже можно отловить на уровне лексера
    // но пока ошибок не возникает
    ''',

    r'''
    string a := 'g
    // не закрывающиеся кавычки сейчас отлавливаются как неизвестный токен
    // потомучто регулярка ищет целую строку вместе с откр и закр кавычками
    ''',

    r'''
    string a := 'g
    // не закрывающиеся кавычки сейчас отлавливаются как неизвестный токен
    // потомучто регулярка ищет целую строку вместе с откр и закр кавычками
    ''',
]


def parse_programm(programm):
    lexer = Lexer(inpt=programm)
    ignore_tokens = (
        TOKEN_TYPES_LIST.newline_token,
        TOKEN_TYPES_LIST.whitesapce_token,
        TOKEN_TYPES_LIST.tabulation_token,
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
    for programm in example_programms:
        try:
            parse_programm(programm)
        except Exception as e:
            print(e)
