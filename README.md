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

## Деплой
Для деплоя используется инструмент ci/cd werf. Werf автоматизирует сборку образа и его доставку в k8s. 

Деплой запускается командой `werf converge --repo omelchenkomaxim/translator-api`.

Перед запуском команды необходимо подключить kubectl к нужному кластеру, подключить docker к нужному registry и прокинуть креды от registry в k8s.

Подробнее с началом работы с werf можно ознакомится [тут](https://ru.werf.io/guides/django/100_basic/20_cluster.html).

Приложение разворачивается по адресу `http://158.160.180.43/translator-api/`


## Локальный запуск
0. Установка python, git
    1. Установить Python 3.12.3: https://www.python.org/downloads/
    2. Установить Git: https://git-scm.com/downloads/
    3. Установить Docker: https://www.docker.com/

1. Клонирование репозитория
```bash
git clone https://github.com/VerkhovtsovDenis/python-translator-api.git
```

2. Создание и настройка виртуального окружения
```bash
cd python-translator-api
python.exe -m pip install --upgrade pip
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

3. Запуск контейнера
```bash
docker compose up -d
```

4. Использование
Перейти по [http://127.0.0.1:5000/docs/](http://127.0.0.1:5000/docs/)
