# EDIT CONFIG

## Описание

Программа для проверки и редактирования конфига `json`.

## Как запустить

1. Запуск прогрммы для чтения конфига
    ` python main.py read путь/имя файла `
2. Запуск прогрммы для редоктирования конфига  ` python main.py write путь/название файла json --param имя_словоря.имя_ключа=значение `

## Содержание

- `main.py` - Файл со скриптом.
- `README` - Файл документации.
- `config.json` - тестовый конфиг.

### Функции в файле main.py

1. `read_config` - функция предназначенная для чтения конфига.

2. `write_config` - функция предназначенная для перезаписи обновлённого файла конфига.

3. `update_config` - функция предназначенная для обновления конфига внутри файла main.py.

4. `main` - Основная функция в которой задаются аргументы и определяет какие функции будут выполняться.

5. `help` - выводит информацию по использованию и синтаксису прогрмаммы

## Примеры использования

1. Четние и вывод конфига

    `python main.py read config.json`

    Вывод:
    ```
        Содержимое конфига:
    {
        "server": {
            "host": "0.0.0.0",
            "port": "100",
            "debug": "false"
        },
        "database": {
            "type": "postgresql",
            "host": "localhost",
            "port": 5432,
            "username": "db_user",
            "password": "db_password",
            "database_name": "my_database"
        },
        "logging": {
            "level": "INFO",
            "file": "/var/log/myapp.log"
        },
        "api": {
            "key": "my_api_key",
            "endpoint": "https://api.example.com/v1/"
        },
        "email": {
            "smtp_server": "smtp.example.com",
            "smtp_port": 587,
            "username": "email_user",
            "password": "email_password",
            "from_email": "no-reply@example.com",
            "to_email": "admin@example.com"
        },
        "features": {
            "enable_feature_x": true,
            "enable_feature_y": false
        }
    }
        ```

2. Изменение параметра 'level' в конфиге  

    `python main.py write config.json --param logging.level=info`

    Вывод: 

    ```
    Конфиг Обновлен
    ``` 

    Было:
    ```
    ...
    },
    "logging": {
        "level": "INFO",
        "file": "/var/log/myapp.log"
    },
    ...
    ```
    Стало:
    ```
    ...
    },
    "logging": {
        "level": "info",
        "file": "/var/log/myapp.log"
    },
    ...
    ```

3. Вывод справки по прогрмамме

    `python main.py -h`

    Вывод:

    ```
        usage: main.py [-h] [--param PARAM] {read,write} filepath

    Работа с файлом конфигурации

    positional arguments:
    {read,write}   действие которое нудно выполнить "read" или "write"
    filepath       путь к файлу конфигурации

    options:
    -h, --help     show this help message and exit
    --param PARAM  Параметр и значение для этого параметра в формате: key.subkey=value (только для write)
    ```


## используемые модули
- ` json ` - Используется для чтения и редактирования фалов .json.
- ` argparse ` - Используется для возможности работы с аргументами в командной строке.  

## Автор
[Колсилкин Михаил](https://github.com/kosilkin/rep)
