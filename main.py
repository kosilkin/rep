import argparse
import json
from textwrap import indent

# DONE: читать фал конфига и выводить в терминал
# TODO: изменять настройк(у/и)
# TODO: Написать документацию
# TODO: написать README

def read_config(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        data = json.load(f)
    return data

def main():
    #создание парсер аргументов - parcer
    parcer = argparse.ArgumentParser(description='Работа с файлом конфигурации')
    # создание аргумента для выбора действия
    # 'название' 'какие аргументы будут возможны'
    parcer.add_argument('action', choices=['read', 'write'])

    # создание аргумента для пути к файлу
    parcer.add_argument('filepath', type=str)
    
    # парсинг аргументов для сохронения в args_action 
    args = parcer.parse_args()

    if args.action == 'read':
        config_data = read_config(args.filepath)
        print(json.dumps(config_data, indent=4))
    elif args.action == 'write':
        print('write')


if __name__ == '__main__':
    main()