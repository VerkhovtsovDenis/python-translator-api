from Translator import Translator
from constants import SupportLanguages


def test_if_without_else():
    pascal_code = "\n".join(
        [
            "var a: integer;",
            "begin",
            "    if a then begin",
            "       a:=1;",
            "    end",
            "end.",
        ]
    )
    python_expected_code = "\n".join(
        [
            "a: int = 0",
            "if a:",
            "    a = 1",
        ]
    )
    
    go_expected_code = "\n".join(
        [
            "package main",
            'import "fmt"',
            "func main() {",
            "    var a int8 = 0",
            "    if a{",
            "        a = 1",
            "    }",
            "}",
        ]
    )

    actual_python_code = Translator.pascla_translate(
        pascal_code, SupportLanguages.PYTHON
    )
    assert python_expected_code.strip() == actual_python_code
    
    actual_go_code = Translator.pascla_translate(
        pascal_code, SupportLanguages.GO
    )
    assert go_expected_code.strip() == actual_go_code


def test_if_without_body():
    pascal_code = "\n".join(
        [
            "var a: integer;",
            "begin",
            "    if a then begin",
            "    end",
            "end.",
        ]
    )
    python_expected_code = "\n".join(
        [
            "a: int = 0",
            "if a:",
            "    pass",
        ]
    )
    go_expected_code = "\n".join(
        [
            "package main",
            'import "fmt"',
            "func main() {",
            "    var a int8 = 0",
            "    if a{",
            "    }",
            "}",
        ]
    )

    actual_python_code = Translator.pascla_translate(
        pascal_code, SupportLanguages.PYTHON
    )
    assert python_expected_code.strip() == actual_python_code
    
    actual_go_code = Translator.pascla_translate(
        pascal_code, SupportLanguages.GO
    )
    assert go_expected_code.strip() == actual_go_code


def test_if_with_else():
    pascal_code = "\n".join(
        [
            "var a: integer;",
            "begin",
            "    if a then begin",
            "        a:=1;",
            "    end",
            "    else begin",
            "        a:=2;",
            "    end",
            "end.",
        ]
    )
    python_expected_code = "\n".join(
        [
            "a: int = 0",
            "if a:",
            "    a = 1",
            "else:",
            "    a = 2",
        ]
    )
    
    go_expected_code = "\n".join(
        [
            "package main",
            'import "fmt"',
            "func main() {",
            "    var a int8 = 0",
            "    if a{",
            "        a = 1",
            "    }",
            "    else{",
            "        a = 2",
            "    }",
            "}",
        ]
    )

    actual_python_code = Translator.pascla_translate(
        pascal_code, SupportLanguages.PYTHON
    )
    assert python_expected_code.strip() == actual_python_code
    
    actual_go_code = Translator.pascla_translate(
        pascal_code, SupportLanguages.GO
    )
    assert go_expected_code.strip() == actual_go_code


def test_if_with_else_without_body():
    pascal_code = "\n".join(
        [
            "var a, b: integer;",
            "begin",
            "    if a>b then begin",
            "        writeln('первое число больше второго');",
            "        if a>10 then begin",
            "            writeln('Первое число больше 10.');",
            "        end",
            "        else begin",
            "            writeln('Первое число меньше или равно 10.');",
            "        end",
            "    end",
            "end.",
        ]
    )
    python_expected_code = "\n".join(
        [
            "a: int = 0",
            "b: int = 0",
            "if a > b:",
            "    print('первое число больше второго')",
            "    if a > 10:",
            "        print('Первое число больше 10.')",
            "    else:",
            "        print('Первое число меньше или равно 10.')",
        ]
    )
    
    go_expected_code = "\n".join(
        [
            "package main",
            'import "fmt"',
            "func main() {",
            "    var a int8 = 0",
            "    var b int8 = 0",
            "    if a > b{",
            '        fmt.Println("первое число больше второго")',
            "        if a > 10{",
            '            fmt.Println("Первое число больше 10.")',
            "        }",
            "        else{",
            '            fmt.Println("Первое число меньше или равно 10.")',
            "        }",
            "    }",
            "}",
        ]
    )

    actual_python_code = Translator.pascla_translate(
        pascal_code, SupportLanguages.PYTHON
    )
    assert python_expected_code.strip() == actual_python_code

    actual_go_code = Translator.pascla_translate(
        pascal_code, SupportLanguages.GO
    )
    assert go_expected_code.strip() == actual_go_code