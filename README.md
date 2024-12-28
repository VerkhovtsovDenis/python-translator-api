## Программа реализована в рамках 2х дисциплин: 
1. Теория языков программирования и компиляторы - выполнена работа над анализом существующих решений и определена методико-теоритическая база создания транслятора с Pascal в Python;
2. Методы коллективной разработки - выполнено создание документации к работающей программе, программа дополнена модулями анализа и трансляции.

## Состояние проекта на текущий момент
Реализивано mvp:
- [x] стандартные операторы
- [x] математические операции
- [x] цикл while
- [x] условия

TODO:
- [] контейниризация двух приложений
- [] массивы
- [] функции
- [] больше модульных тестов
- [] end to end тесты

## Запуск

`docker compose up`

документация доступна по `http://127.0.0.1:8000/docs/`

## Api
эндпоинт - post `http://localhost:8000/translate`
тело запроса:
```
    {
        "pascal_code": "string",
        "target_language": "python"
    }
```

пример запроса:
```
    {
        "pascal_code": "var a, b: integer; begin b:=(a+7)*8; write(b); end.",
        "target_language": "python"
    }
```
пример ответа:
```
    {
        "result_code": "b: int = (a + 7) * 8\nprint(b, sep='')\n",
        "erors": ""
    }
```
пример запроса:
```
    {
    "pascal_code": "var a, a: integer; begin b:=(a+7)*8; write(b); end.",
    "target_language": "python"
    }
```
пример ответа:
```
    {
    "result_code": "",
    "erors": "Semantic error, Re-declared identifier 'a'."
    }
```

## Docstrings Style
```
def layout(dash_app: Dash) -> filters_layout.FiltersLayout:
    """
    Формирование макета приложения.

    Args:
        dash_app (Dash): Dash приложение, для которого необходим макет.

    Returns:
        FiltersLayout: Готовый экземпляр макета с необходимыми фильтрами.
    """
```

```
def transform_as_tree(
        self,
        group_column: str,
        group_default_expanded: int = 0,
        function_path: str = "params['%(group_column)s']",
    ) -> None:
        """
        Преобразовываем AgGrid в древовидную таблицу.

        Args:
            group_column (str): Колонка, по которой происходит группировка.
            group_default_expanded (int, optional): Раскрытие уровней по умолчанию.
                По умолчанию: 0.
            function_path (str, optional): Функция, которая возвращает список значений дерева.
                Чаще всего это просто значение из колонки, так как там как раз данные в виде:
                ['Значение первого уровня', 'Значение второго уровня', ...].
                По умолчанию: params['%(group_column)s'].
        """
```

```
def __init__(
    self,
    filter_components: list[SidebarFilterComponent] | None = None,
    body_children: Any | None = None,
    is_open_sidebar: bool = True,
    dash_app: Dash | None = None,
    filters_id: str | None = None,
    is_force_init_callbacks: bool = True,
    **kwargs,
) -> None:
    """
    Args:
        filter_components (list[SidebarFilterComponent] | None, optional): Список с фильтрами.
            По умолчанию: None.
        body_children (Any | None, optional): Содержимое макета. По умолчанию: None.
        is_open_sidebar (bool, optional): Открыт сайдбар с фильтрами по умолчанию.
            По умолчанию: True.
        dash_app (Dash | None, optional): Dash приложение, в которое надо добавить колбеки.
            По умолчанию: None.
            Необходим, если is_force_init_callbacks = True.
        filters_id (str | None, optional): Идентификатор фильтров (основного элемента, 
            в котором содержится кнопка применить и storage со значениями всех фильтров).
            По умолчанию: None.
        is_force_init_callbacks (bool, optional): Принудительно инициализировать колбеки 
            при инициализации объекта.
            По умолчанию: True.

    Raises:
        ValueError: Dash app required for force init callbacks.
    """
```

```
def init_callback(self, dash_app: dash.Dash, filter_id: str, filters_storage_id: str) -> None:
    """
    Метод для инициализации колбеков фильтра.

    Args:
        dash_app (dash.Dash): Dash приложение, в которое необходимо добавить колбеки.
        filter_id (str): Идентификатор фильтра.
        filters_storage_id (str): Идентификатор storage, в котором хранятся все фильтры.

    Raises:
        NotImplementedError: Метод не реализован.
    """
```