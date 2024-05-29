import argparse
import json

# DONE: читать фал конфига и выводить в терминал
# DONE: изменять настройк(у/и)
# DONE: Написать документацию
# TODO: написать README

def read_config(filepath):
    try:
        with open(filepath, 'r', encoding='utf8') as f:
            data = json.load(f)
        return data
    except: print('Ошибка в открытии файла, проверте наличие конфига или путь к ниму')
# pfgзапись конфига в файл
def write_config(filepath, config):
    try:
        with open(filepath, 'w', encoding='utf8') as f:
            json.dump(config, f, indent=4)
    except: print('Ошибка в открытии файла, проверте наличие конфига или путь к ниму')

# изменение параметра в конфиге
def update_config(config, param, value):
    try:
        keys = param.split('.') # путь к параметру
        for key in keys[:-1]: # прохадим по всем ключам кроме последнего
            # переходи на следующий уровень вложенности. Если ключа нет, то создаём пустой словарь
            data = config.setdefault(key, {})
        data[keys[-1]] = value # устанавливаем значение для послднего ключа
    except: print('Ошибка в открытии файла, проверте наличие конфига или путь к ниму')

def main():
    #создание парсер аргументов - parcer
    parcer = argparse.ArgumentParser(description='Работа с файлом конфигурации')

    # создание аргумента для выбора действия
    parcer.add_argument('action', choices=['read', 'write'], help='действие которое нудно выполнить "read" или "write"')
    # создание аргумента для пути к файлу
    parcer.add_argument('filepath', type=str, help='путь к файлу конфигурации')
    # создание аргумента для параметра и его знач
    parcer.add_argument('--param', type=str, help='Параметр и значение для этого параметра в формате: key.subkey=value (только для write)')
    
    # парсинг аргументов для сохронения в args_action 
    args = parcer.parse_args()

    if args.action == 'read':
        config_data = read_config(args.filepath)
        print('Содержимое конфига:')
        print(json.dumps(config_data, indent=4))
    elif args.action == 'write':
        try:
            config_data = read_config(args.filepath)
            path, value = args.param.split('=')
            update_config(config_data, path, value)
            write_config(args.filepath, config_data)
            print('Конфиг Обновлен')
        except: print('Не верно введены аргументы, что бы узнать синтаксис введите "python main.py -h"')

if __name__ == '__main__':
    main()