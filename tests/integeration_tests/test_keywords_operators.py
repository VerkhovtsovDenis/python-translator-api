from Translator import Translator
from constants import SupportLanguages


def test_keywords_operator():
    pascal_code = "\n".join(
        [
            "program aaa;",
            "var a, b: real;",
            "begin",
            "",
            "a := 9.0;",
            "b := 10.2;",
            "writeln(a +  b);",
            "end.",
        ]
    )
    python_expected_code = "\n".join(
        [
            "a: float = 0.0",
            "b: float = 0.0",
            "a = 9.0",
            "b = 10.2",
            "print(a + b)",
        ]
    )

    actual_python_code = Translator.pascla_translate(
        pascal_code, SupportLanguages.PYTHON
    )
    assert python_expected_code.strip() == actual_python_code


def test_keywords_operator_with_nested_brackets():
    pascal_code = "\n".join(
        [
            "program aaa;",
            "var a, b: real;",
            "begin",
            "",
            "a := 9.0;",
            "b := 10.2;",
            "writeln((a +  b) * b, b, (a + b) * a);",
            "end.",
        ]
    )
    python_expected_code = "\n".join(
        [
            "a: float = 0.0",
            "b: float = 0.0",
            "a = 9.0",
            "b = 10.2",
            "print((a + b) * b, b, (a + b) * a)",
        ]
    )

    actual_python_code = Translator.pascla_translate(
        pascal_code, SupportLanguages.PYTHON
    )
    assert python_expected_code.strip() == actual_python_code