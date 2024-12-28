from Translator import Translator
from constants import SupportLanguages


def test_while():
    pascal_code = "\n".join(
        [
            "var a: integer;",
            "begin",
            "    while a do begin",
            "       a:=1;",
            "    end",
            "end.",
        ]
    )
    python_expected_code = "\n".join(
        [
            "a: int = 0",
            "while a:",
            "    a = 1",
        ]
    )

    actual_python_code = Translator.pascla_translate(
        pascal_code, SupportLanguages.PYTHON
    )
    assert python_expected_code.strip() == actual_python_code


def test_while_without_body():
    pascal_code = "\n".join(
        [
            "var a: integer;",
            "begin",
            "    while a do begin",
            "    end",
            "end.",
        ]
    )
    python_expected_code = "\n".join(
        [
            "a: int = 0",
            "while a:",
            "    pass",
        ]
    )

    actual_python_code = Translator.pascla_translate(
        pascal_code, SupportLanguages.PYTHON
    )
    assert python_expected_code.strip() == actual_python_code


def test_nested_while():
    pascal_code = "\n".join(
        [
            "var a, b: integer;",
            "begin",
            "    while a>b do begin",
            "        writeln('первое число больше второго');",
            "        while a>10 do begin",
            "            writeln('Первое число больше 10.');",
            "        end",
            "    end",
            "end.",
        ]
    )
    python_expected_code = "\n".join(
        [
            "a: int = 0",
            "b: int = 0",
            "while a > b:",
            "    print('первое число больше второго')",
            "    while a > 10:",
            "        print('Первое число больше 10.')",
        ]
    )

    actual_python_code = Translator.pascla_translate(
        pascal_code, SupportLanguages.PYTHON
    )
    assert python_expected_code.strip() == actual_python_code
